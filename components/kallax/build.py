"""Audit, render and publish a deterministic versioned KALLAX assembly package."""
from collections import Counter
from pathlib import Path
import copy, csv, fnmatch, hashlib, json, shutil, subprocess
from PIL import Image
from .instances import define_instances
from .assembly_cards import ROOT

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def prepare(**kwargs):
    config=copy.deepcopy(kwargs['configuration'])
    folder=ROOT/'parts'/config['id']
    output=folder/'assembly'
    for sub in ['render/raw','render/scenes','readme','assets']:(output/sub).mkdir(parents=True,exist_ok=True)
    records=define_instances()
    lookup={r['name']:r for r in records}
    actual=Counter(r['part'] for r in records)
    parts=config['parts']
    assert actual==Counter({k:p['quantity'] for k,p in parts.items()}), 'Physical BOM mismatch'
    def select(patterns):
        selected=[]
        for pattern in patterns:
            matches=[n for n in lookup if fnmatch.fnmatchcase(n,pattern)]
            if not matches:raise ValueError('No physical instance matches '+pattern)
            selected.extend(matches)
        if len(selected)!=len(set(selected)):raise ValueError('Duplicate selector')
        return selected
    seen=set(); steps=[]
    for number, definition in enumerate(config['steps'],1):
        step=copy.deepcopy(definition)
        added=select(step['add'])
        assert not seen.intersection(added), 'Item introduced twice'
        seen.update(added)
        offsets={n:[v*config['style']['explosion_scale'] for v in vec] for pattern,vec in step['move'].items() for n in select([pattern])}
        assert set(offsets)<=seen
        step.update(number=number,key=f'step_{number:02d}',added_instances=added,shown_instances=[n for n in lookup if n in seen],offsets=offsets,loose_parts=dict(Counter(lookup[n]['part'] for n in added)))
        assert len(step['loose_parts'])<=4
        steps.append(step)
    assert seen==set(lookup), 'Unintroduced items'
    source_hashes={p['stl']:digest(ROOT/p['stl']) for p in parts.values() if 'stl' in p}
    for key,part in parts.items():
        part['key']=key
        if part.get('printed'):
            assert not any(k in part for k in ['short_url','md5_6_alpha'])
        elif part.get('short_url'):
            md5=hashlib.md5(part['id'].encode()).hexdigest(); value=int(md5[:6],16); alpha=''
            while value: value,n=divmod(value,36); alpha='0123456789abcdefghijklmnopqrstuvwxyz'[n]+alpha
            assert alpha==part['md5_6_alpha'], 'OOMP code does not match identity'
            part.update(md5=md5,short_label='oom.lt/a/'+alpha)
        else:
            assert key=='H1' and part['catalogue_status']=='pending'
    data=dict(style=config['style'],book=config['book'],configuration_title=config['readme']['title'],parts=parts,printed_keys=[k for k,p in parts.items() if p.get('printed')],steps=steps,instances=records,physical_item_count=len(records),source_sha256=source_hashes,readme=config['readme'])
    render_spec=dict(source=source_hashes,instances=records,steps=[{k:s[k] for k in ['shown_instances','offsets']} for s in steps],style=config['style'],renderer={n:digest(Path(__file__).with_name(n)) for n in ['render_studio.py','cad.py']})
    data['render_signature']=hashlib.sha256(json.dumps(render_spec,sort_keys=True).encode()).hexdigest()
    scripts = [ROOT / name for name in ("action_make_all.py", "working.py", "working_oomp_populate.py", "working_oomp.py", "working_scad.py")]
    data['generator_sha256']={str(p.relative_to(ROOT)):digest(p) for p in [*scripts,ROOT/config['book']['logo_svg'],*Path(__file__).parent.glob('*.py'),Path(__file__).with_name('assembly_viewer.html')]}
    data['identity_notes']='Hardware codes use existing OOMP identities. Redirects are not registered by this build. M6 x 300 rod remains pending by user instruction. Printed parts have no codes.'
    (output/'assembly_manifest.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    with (output/'parts.csv').open('w',newline='',encoding='utf-8') as handle:
        writer=csv.DictWriter(handle,fieldnames=['key','name','detail','quantity','id','stl','md5','md5_6_alpha','short_url','url','catalogue_status','identity_source'])
        writer.writeheader()
        writer.writerows({k:p.get(k,'') for k in writer.fieldnames} for p in parts.values())
    return folder,output,data

def main(**kwargs):
    folder,output,data=prepare(**kwargs)
    cache=output/'render/validation.json'
    if kwargs.get('render',True):
        blender=kwargs.get('blender') or shutil.which('blender')
        if not blender:raise RuntimeError('Blender is required on PATH')
        with (output/'render/blender.log').open('w',encoding='utf-8') as log:
            subprocess.run([blender,'--background','--factory-startup','--python-exit-code','1','--python',str(Path(__file__).with_name('render_studio.py')),'--',str(output)],stdout=log,stderr=subprocess.STDOUT,check=True)
        raw_files=sorted((output/'render/raw').glob('*.png'))
        cache.write_text(json.dumps({'signature':data['render_signature'],'images':{p.name:digest(p) for p in raw_files}},indent=2))
    else:
        checked=json.loads(cache.read_text())
        if checked['signature']!=data['render_signature']:raise ValueError('Render recipe or source meshes changed; run python working.py')
        for name,sha in checked['images'].items():
            if digest(output/'render/raw'/name)!=sha:raise ValueError('Stale or altered render: '+name)
    from .assembly_booklet import publish,review_outputs
    publish(output=output,data=data)
    review_outputs(output=output,data=data)
    from .assembly_viewer import publish as viewer
    viewer(output=output,data=data)
    for name in ['cell','cabinet','printed','exploded']:
        src=output/'render/raw'/(name+'.png')
        shutil.copyfile(src,output/'readme'/(name+'.png'))
    for key in data['printed_keys']:
        part = data['parts'][key]
        component_dir = (ROOT / part['stl']).parent
        # Component pages retain their individual print downloads.
        kit_link = f"../{folder.name}/README.md"
        note = (f"# {part['name']}\n\n{part['detail']}. Print {part['quantity']} in black for one cell.\n\n"
                f"[Print STL](3dpr.stl) | [OpenSCAD source](3dpr.scad) | [Complete kit]({kit_link})\n")
        (component_dir/'readme.md').write_text(note, encoding='utf-8')
    with Image.open(output/'readme/cell.png') as image:
        image.thumbnail((480,480));image.save(output/'readme/thumbnail.png')
    from .documentation import publish as documentation
    from .print_project import publish as pack_print_project
    pack_print_project(folder, data)
    documentation(folder=folder,output=output,data=data)
    report=json.loads((output/'validation.json').read_text())
    report.update(source_sha256=data['source_sha256'],render_signature=data['render_signature'],cumulative_inventory_verified=True,hosting='Not published; standalone HTML generated')
    (output/'validation.json').write_text(json.dumps(report,indent=2))
    from .validate import main as validate
    validate(output=output)
    print('Built',output/'assembly_instructions.pdf',flush=True)
    return output
