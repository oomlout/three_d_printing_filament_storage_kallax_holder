import bpy,json
from pathlib import Path
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
ROOT=Path(__file__).resolve().parent
anchors={
 'empty':{'A':(-163,-10,22),'B':(163,187,60),'C':(0,-67.5,37)},
 'rail':{'rod':(-30,0,80),'long':(-135,-15,30),'centre':(-30,-15,30),'nut':(190,-15,30),'grip':(156,-15,30),'bolt':(269,-15,30),'fixed':(-206,-15,30),'clip':(226,-15,30)},
 'exploded':{'side':(170,0,22),'sleeves':(0,-67.5,37),'coupling':(211.5,-67.5,37),'grip':(250.5,-67.5,37)}
}
for shot,points in anchors.items():
 bpy.ops.wm.open_mainfile(filepath=str(ROOT/'renders/scenes'/f'{shot}.blend'))
 scene=bpy.context.scene;out={}
 for k,p in points.items():
  v=world_to_camera_view(scene,scene.camera,Vector(p)*.001);out[k]=[v.x,1-v.y]
 (ROOT/'renders/raw'/f'{shot}_anchors.json').write_text(json.dumps(out,indent=2))
