"""Render the populated physical-instance sequence with the existing CAD meshes."""
from pathlib import Path
import sys, json, math
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from components.kallax import cad as r
from mathutils import Vector, Matrix
import bpy

output = Path(sys.argv[sys.argv.index('--')+1])
data = json.loads((output/'assembly_manifest.json').read_text())
raw = output/'render/raw'
raw.mkdir(parents=True, exist_ok=True)
scene = r.scene
scene.cycles.samples = data['style']['samples']
scene.render.film_transparent = True
bpy.context.preferences.filepaths.save_version = 0
# Catalogue STL paths are authoritative. Legacy scad_output names are only lookup aliases.
source_map = {p['id'].replace('project_github_oomlout_three_d_printing_filament_storage_kallax_', ''): ROOT/p['stl'] for p in data['parts'].values() if 'stl' in p}
def cad(part, name, loc=(0,0,0), rot=None):
    if part not in r.cache:
        bpy.ops.wm.stl_import(filepath=str(source_map[part]))
        obj=bpy.context.object
        obj.data.transform(Matrix.Scale(.001,4))
        obj.data.materials.clear(); obj.data.materials.append(r.black)
        r.cache[part]=obj.data
        bpy.data.objects.remove(obj,do_unlink=True)
    obj=bpy.data.objects.new(name,r.cache[part]); scene.collection.objects.link(obj)
    obj.location=r.V(loc)
    if rot is not None: obj.rotation_euler=rot
    r.bevel(obj,.15)
    return obj
r.cad=cad

objects={}
for rec in data['instances']:
    before=set(scene.objects)
    p=rec['part']; x,y,z=rec['pos']
    if p in ['P1','P2']:
        cad(r.SHORT if p=='P1' else r.TALL,rec['name'],(x,y,z),r.END_ROT if rec['reverse'] else r.SIDE_ROT)
    elif p.startswith('P'):
        length,extra={'P3':(99.67,'one_end_nut'),'P4':(67.67,'one_end_nut'),'P5':(18,'full_nut'),'P6':(11,'full_nut'),'P7':(11,'slotted_overlap')}[p]
        obj=r.spacer(length,(x,y,z),extra,rec['reverse'],rec['name'])
        if p=='P7':obj.rotation_euler=Matrix(((0,0,1),(-1,0,0),(0,-1,0))).to_euler()
    elif p=='H1':r.thread(rec['name'],x,y,z,300)
    elif p in ['H2','H3']:r.coupling(x,y,z,5 if p=='H2' else 18,rec['name'])
    elif p=='H4':r.adjustment_bolt(x,y,z)
    objects[rec['name']]=list(set(scene.objects)-before)
    for obj in objects[rec['name']]:obj['physical_instance']=rec['name']
original={o.name:o.location.copy() for group in objects.values() for o in group}
r.lighting((0,85,70),.9)
r.camera((0,85,70),(600,-800,675),600)
camera=scene.camera
eye=Vector(data['style']['eye']).normalized()

def render(name, included, offsets=None, size=(1500,1100)):
    offsets=offsets or {}
    for key,group in objects.items():
        for obj in group:
            obj.hide_render=key not in included
            obj.location=original[obj.name]+r.V(offsets.get(key,[0,0,0]))
    bpy.context.view_layer.update()
    pts=[o.matrix_world@Vector(corner) for key in included for o in objects[key] for corner in o.bound_box]
    target=sum(pts,Vector())/len(pts)
    camera.location=target+eye
    camera.rotation_euler=(-eye).to_track_quat('-Z','Y').to_euler()
    bpy.context.view_layer.update()
    inv=camera.matrix_world.inverted()
    campts=[inv@p for p in pts]
    low=[min(p[i] for p in campts) for i in (0,1)]
    high=[max(p[i] for p in campts) for i in (0,1)]
    shift=camera.rotation_euler.to_matrix()@Vector(((low[0]+high[0])/2,(low[1]+high[1])/2,0))
    camera.location+=shift
    aspect=size[0]/size[1]
    camera.data.ortho_scale=max(high[0]-low[0],(high[1]-low[1])*aspect)*1.12
    scene.render.resolution_x,scene.render.resolution_y=size
    scene.render.filepath=str(raw/(name+'.png'))
    bpy.ops.render.render(write_still=True)

for step in data['steps']:
    render(step['key'],step['shown_instances'],step['offsets'])
    # One editable scene per operation, with physical-instance metadata.
    scene.render.filepath = "//../raw/" + step["key"] + ".png"
    bpy.ops.wm.save_as_mainfile(filepath=str(output/'render/scenes'/(step['key']+'.blend')), relative_remap=False)
for key in data['parts']:
    instance=next(rec['name'] for rec in data['instances'] if rec['part']==key)
    render('part_'+key,[instance],size=(480,360))
render('book_cover',list(objects),size=(1800,1200))
scene.render.filepath = "//../raw/book_cover.png"
bpy.ops.wm.save_as_mainfile(filepath=str(output/'render/scenes/assembled.blend'), relative_remap=False)


# Render the same revised meshes in the installed and printed-only views.
def reset_scene():
    for obj in list(scene.objects):
        bpy.data.objects.remove(obj, do_unlink=True)

def context_image(name):
    scene.render.resolution_x = 1600
    scene.render.resolution_y = 1150
    scene.render.film_transparent = False
    r.cube('Studio floor',(0,0,-10),(20000,20000,20),r.paper,0)
    scene.render.filepath = str(raw/(name+'.png'))
    bpy.ops.render.render(write_still=True)

reset_scene()
r.printed_scene()
context_image('printed')
reset_scene()
r.hardware_scene()
context_image('exploded')

reset_scene()
w,b=r.shelf(1)
r.cradle(0,-93.5,b)
r.cradle(0,93.5,b,True)
cols=(r.teal,r.yellow,r.dark,r.teal,r.yellow)
for i,col in enumerate(cols):
    r.spool((i-2)*62,-93.5,b+120.01,col,i)
    r.refill((i-2)*62,93.5,b+195.01,cols[4-i],i)
r.camera((0,-20,214),(260,-1000,220),740);r.lighting((0,0,210),.85)
context_image('cell')

reset_scene()
w,b=r.shelf(4)
for cell,colset in [((1,1),(r.teal,r.yellow,r.dark,r.teal,r.yellow)),((2,2),(r.yellow,r.teal,r.dark,r.yellow,r.teal))]:
    c,row=cell;cx=-w/2+b+c*351+167.5;bz=b+row*351
    r.cradle(cx,-93.5,bz)
    r.cradle(cx,93.5,bz,True)
    for i,col in enumerate(colset):
        r.spool(cx+(i-2)*62,-93.5,bz+120.01,col,i)
        r.refill(cx+(i-2)*62,93.5,bz+195.01,colset[4-i],i)
r.camera((0,0,w*.49),(1500,-4600,1300),2250);r.lighting((0,0,w*.5),2.7)
context_image('cabinet')
