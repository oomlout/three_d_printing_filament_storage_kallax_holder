"""Align hex pockets in saved revision scenes and audit assembly counts."""
import bpy,math,json
from pathlib import Path
from mathutils import Matrix
root=Path(__file__).resolve().parents[2]
report={}
for shot in ('empty','cell','cabinet','loaded','rail','exploded','adjust'):
    bpy.ops.wm.open_mainfile(filepath=str(root/'renders/scenes'/f'{shot}.blend'))
    scene=bpy.context.scene
    for o in scene.objects:
        if o.name.startswith(('A |','B |','C |','Printed sleeve')):
            reverse=(o.rotation_euler.to_matrix()@__import__('mathutils').Vector((0,0,1))).x<0
            mat=Matrix(((0,0,-1),(1,0,0),(0,-1,0))) if reverse else Matrix(((0,0,1),(1,0,0),(0,1,0)))
            o.rotation_euler=mat.to_euler()
        if o.name.startswith(('M6 coupling nut','M6 captive fixed-end nut')):
            o.rotation_euler[0]=math.pi/6
    names=[o.name for o in scene.objects]
    counts={key:sum(n.startswith(prefix) for n in names) for key,prefix in {
       'short_frames':'Short side frame','tall_frames':'Tall side frame',
       'coupling_nuts':'M6 coupling nut','fixed_nuts':'M6 captive fixed-end nut',
       'adjustment_bolts':'Adjustment bolt |','rod_cores':'M6 x 300 mm threaded rod core'}.items()}
    report[shot]=counts
    if shot in ('cell','loaded','empty'):
        assert counts==dict(short_frames=4,tall_frames=4,coupling_nuts=4,fixed_nuts=4,adjustment_bolts=4,rod_cores=4),counts
    if shot=='cabinet':
        assert counts==dict(short_frames=8,tall_frames=8,coupling_nuts=8,fixed_nuts=8,adjustment_bolts=8,rod_cores=8),counts
    bpy.ops.wm.save_as_mainfile(filepath=str(root/'renders/scenes'/f'{shot}.blend'))
    scene.render.filepath=str(root/'renders/raw'/f'{shot}.png')
    bpy.ops.render.render(write_still=True)
(root/'renders/qa/assembly_counts.json').write_text(json.dumps(report,indent=2))
