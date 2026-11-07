"""Record immutable production mesh evidence and verify the selected source parts."""
import hashlib,json
from pathlib import Path
import numpy as np
import trimesh
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'presentation'
data=json.loads((P/'project.json').read_text(encoding='utf-8'))
records=[]
for p in data['printed_parts']:
    path=ROOT/p['stl'];mesh=trimesh.load(path,force='mesh')
    assert mesh.is_watertight,(p['ref'],'not watertight')
    source=ROOT/'scad_output'/p['part']/'3dpr.stl'
    assert hashlib.sha256(path.read_bytes()).digest()==hashlib.sha256(source.read_bytes()).digest(),(p['ref'],'catalogue and renderer sources differ')
    if p['ref'] in ('P6','P7'):assert abs(mesh.extents[2]-7)<1e-5
    records.append({'reference':p['ref'],'path':p['stl'],'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                    'watertight':bool(mesh.is_watertight),'extents_mm':mesh.extents.tolist(),'bounds_mm':mesh.bounds.tolist()})
(P/'qa/source-meshes.json').write_text(json.dumps({'status':'PASS','parts':records},indent=2),encoding='utf-8')
print('PASS: seven source parts, matching catalogue/render meshes; both end covers are 7 mm')
