"""Read-only checks of frame counts and recessed fastener seating."""
import bpy,json
from pathlib import Path
from mathutils import Vector
root=Path(__file__).resolve().parents[2]
report={}
for shot,multiplier in [('cell',1),('empty',1),('loaded',1),('cabinet',2)]:
    bpy.ops.wm.open_mainfile(filepath=str(root/'renders/scenes'/f'{shot}.blend'))
    objects=list(bpy.context.scene.objects)
    expected={'Short side frame':4,'Tall side frame':4,'M6 coupling nut':4,
              'M6 captive fixed-end nut':4,'Adjustment bolt |':4,
              'M6 x 300 mm threaded rod core':4,'D | 14 mm slip-on cover':4}
    counts={p:sum(o.name.startswith(p) for o in objects) for p in expected}
    assert all(counts[p]==expected[p]*multiplier for p in expected),counts
    if multiplier==1:
        for o in objects:
            if o.name.startswith('Adjustment bolt |'):
                xs=[(o.matrix_world@Vector(v)).x*1000 for v in o.bound_box]
                assert abs(min(xs)-162.505)<.02 and abs(max(xs)-166.505)<.02,xs
            if o.name.startswith('M6 captive fixed-end nut'):
                xs=[(o.matrix_world@Vector(v)).x*1000 for v in o.bound_box]
                assert abs(min(xs)+167.505)<.02 and abs(max(xs)+162.505)<.02,xs
    report[shot]=counts
report['axial_mm']={'printed_span':335.01,'bolt_length':25,'coupler_length':18,
 'cover_length':14,'rod_engagement':5.99,'bolt_engagement':7,'tip_gap':5.01,
 'head_recess_depth':5,'nominal_head_thickness':4,'head_recess_below_face':1}
(root/'renders/qa/assembly_counts.json').write_text(json.dumps(report,indent=2))
print('PASS: scene counts, slot covers, recessed head/nut positions')
