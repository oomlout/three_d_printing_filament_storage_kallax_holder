"""Create a three-plate Bambu Studio project from the retained empty P1S project."""
import copy
import hashlib
import os
import subprocess
from tempfile import TemporaryDirectory
import io
import json
import shutil
import zipfile
from collections import Counter
from pathlib import Path
import xml.etree.ElementTree as ET

import numpy as np
import trimesh
from PIL import Image, ImageDraw

from .assembly_cards import ROOT
from .p1s_print_kit import add_printable_copy, validate_kit_archive

PROJECT_FILENAME = 'working.3mf'

NS = 'http://schemas.microsoft.com/3dmanufacturing/core/2015/02'
ET.register_namespace('', NS)
def core(name):
    return '{' + NS + '}' + name

def metadata(parent, key, value):
    return ET.SubElement(parent, 'metadata', key=key, value=str(value))

def placements():
    # Flat frames. Pockets face upwards. Sleeves stand on their flat ends.
    for i in range(4):
        yield 'P1', 1, 80, 55+i*52
    for i in range(4):
        yield 'P2', 2+i//2, 100, 64+(i%2)*128
    i=0
    for key, count in [('P3',8),('P4',4),('P5',4),('P6',4),('P7',4)]:
        for _ in range(count):
            yield key, 1, 181+(i%3)*28, 34+(i//3)*27
            i+=1

def xml(element):
    return ET.tostring(element,encoding='utf-8',xml_declaration=True)

def publish(folder, data):
    source = ROOT/'source_file/default.3mf'
    dest = folder / PROJECT_FILENAME
    print_dir = folder/'print'
    print_dir.mkdir(exist_ok=True)
    template = zipfile.ZipFile(source)
    settings_bytes = template.read('Metadata/project_settings.config')
    settings = json.loads(settings_bytes)
    assert settings['printer_model']=='Bambu Lab P1S' and settings['nozzle_diameter']==['0.4']
    assert settings['filament_colour'][0]=='#000000'
    model = ET.Element(core('model'),unit='millimeter',attrib={'xml:lang':'en-US'})
    for key,value in [('Application','BambuStudio-02.09.02.62'),('BambuStudio:3mfVersion','1'),('Title','KALLAX filament holders - one cell')]:
        ET.SubElement(model,core('metadata'),name=key).text=value
    resources=ET.SubElement(model,core('resources'))
    build=ET.SubElement(model,core('build'))
    config=ET.Element('config')
    meshes={}
    geometry_by_key={}
    for key in data['printed_keys']:
        part=data['parts'][key]
        stl=ROOT/part['stl']
        shutil.copyfile(stl, print_dir/(key+'.stl'))
        mesh=trimesh.load(stl,force='mesh')
        assert mesh.is_watertight and len(mesh.split())==1
        # Frames and one-end sleeves have 5 mm nut recesses on the CAD bottom.
        if key in ("P1", "P2", "P3", "P4"):
            mesh.apply_transform(np.diag([1, -1, -1, 1]))  # Half turn about X.
        # Centre the oriented part and seat its lowest face on the bed.
        mesh.apply_translation([-mesh.bounds[:,0].mean(),-mesh.bounds[:,1].mean(),-mesh.bounds[0,2]])
        meshes[key]=mesh
        geometry=ET.Element(core('mesh'))
        geometry_by_key[key]=geometry
        vertices=ET.SubElement(geometry,core('vertices'))
        for x,y,z in mesh.vertices:
            ET.SubElement(vertices,core('vertex'),x=f'{x:.7f}',y=f'{y:.7f}',z=f'{z:.7f}')
        triangles=ET.SubElement(geometry,core('triangles'))
        for a,b,c in mesh.faces:
            ET.SubElement(triangles,core('triangle'),v1=str(a),v2=str(b),v3=str(c))
    plate_template=ET.fromstring(template.read('Metadata/model_settings.config')).find('plate')
    plates={}; previews={}; bounds={}; counts=Counter()
    origins={1:(0,0),2:(307.2,0),3:(0,-307.2)}
    for num,name in enumerate(['Short frames and spacers','Tall frames A','Tall frames B'],1):
        plate=copy.deepcopy(plate_template)
        for m in list(plate):
            k=m.get('key','')
            if k in ['pick_file','top_file','thumbnail_no_light_file']:plate.remove(m)
            elif k=='thumbnail_file':m.set('value',f'Metadata/plate_{num}.png')
            elif k=='plater_id':m.set('value',str(num))
            elif k=='plater_name':m.set('value',name)
        config.append(plate);plates[num]=plate
        previews[num]=Image.new('RGB',(512,512),'#eeeeea')
        bounds[num]=[(0,0,18,28)]
    for ident,(key,num,x,y) in enumerate(placements(),1):
        mesh=meshes[key]
        low,high=mesh.bounds
        box=(x+low[0],y+low[1],x+high[0],y+high[1])
        assert min(box[:2])>=3 and max(box[2:])<=253
        assert all(box[0]>=b[2]+3 or box[2]<=b[0]-3 or box[1]>=b[3]+3 or box[3]<=b[1]-3 for b in bounds[num])
        bounds[num].append(box)
        ox,oy=origins[num]
        part = data['parts'][key]
        add_printable_copy(
            serial=ident,
            name=f"{part['name']} ({counts[key]+1} of {part['quantity']})",
            mesh=geometry_by_key[key], resources=resources, build=build, settings=config,
            plate=plates[num], transform=f'1 0 0 0 1 0 0 0 1 {x+ox} {y+oy} 0', filament=1,
        )
        counts[key]+=1
        draw=ImageDraw.Draw(previews[num])
        # Top-facing triangles yield the actual plate silhouette, including holes.
        for triangle,normal in zip(mesh.triangles,mesh.face_normals):
            if normal[2]>0.01:
                draw.polygon([(round(2*(x+v[0])),round(512-2*(y+v[1]))) for v in triangle], fill='#27282a')
    assert counts==Counter({k:data['parts'][k]['quantity'] for k in data['printed_keys']})
    with zipfile.ZipFile(dest.with_suffix('.tmp'),'w',zipfile.ZIP_DEFLATED) as out:
        for name in ['[Content_Types].xml','_rels/.rels','Metadata/slice_info.config']:
            out.writestr(name,template.read(name))
        out.writestr('Metadata/project_settings.config',settings_bytes)
        out.writestr('3D/3dmodel.model',xml(model));out.writestr('Metadata/model_settings.config',xml(config))
        out.writestr('Metadata/filament_sequence.json',json.dumps({f'plate_{n}':{'sequence':[]} for n in plates}))
        for num,im in previews.items():
            for suffix,size in [('',512),('_small',128)]:
                stream=io.BytesIO();im.resize((size,size),Image.Resampling.LANCZOS).save(stream,format='PNG')
                out.writestr(f'Metadata/plate_{num}{suffix}.png',stream.getvalue())
    template.close()
    validate_kit_archive(dest.with_suffix('.tmp'), count=sum(counts.values()))
    dest.with_suffix('.tmp').replace(dest)


def validate_slice(folder):
    """Slice the editable project with its embedded defaults and keep the report."""
    binary = shutil.which("bambu-studio")
    if not binary:
        binary = Path(os.environ.get("ProgramFiles", "")) / "Bambu Studio" / "bambu-studio.exe"
    if not Path(binary).is_file():
        raise FileNotFoundError("Install Bambu Studio or put bambu-studio on PATH to slice the kit.")
    project = folder / PROJECT_FILENAME
    starter = ROOT / "source_file/default.3mf"
    with zipfile.ZipFile(project) as kit, zipfile.ZipFile(starter) as template:
        settings = "Metadata/project_settings.config"
        if kit.read(settings) != template.read(settings):
            raise ValueError("P1S project settings differ from the starter")
        geometry_hash = hashlib.sha256(kit.read("3D/3dmodel.model")).hexdigest()
    with TemporaryDirectory() as temp:
        subprocess.run([str(binary), "--slice", "0", "--outputdir", temp, str(project)], check=True)
        result = json.loads((Path(temp) / "result.json").read_text(encoding="utf-8"))
        plates = result["sliced_plates"]
        if result["return_code"] or sorted(p["id"] for p in plates) != [1, 2, 3]:
            raise ValueError("Bambu Studio did not slice all three plates successfully")
        for plate in plates:
            gcode = Path(temp) / f"plate_{plate['id']}.gcode"
            if plate["warning_message"] or not gcode.is_file() or not gcode.stat().st_size:
                raise ValueError(f"Plate {plate['id']} failed validation: {plate['warning_message']}")
    report = dict(printer="Bambu Lab P1S", default_template_sha256=hashlib.sha256(starter.read_bytes()).hexdigest(),
                  geometry_and_placement_sha256=geometry_hash, settings_identical=True, slicer=result)
    (folder / "print/slice_validation.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

