"""Historical revision-1 generator; not used by the current presentation build.
Revision 2 uses the existing 7 mm hex nut cover and 7 mm slotted cover.
Create a 14 mm slotted end cover from the original 9 mm constant-section print.
No original part is modified. Regeneration uses the source mesh and SCAD profile.
"""
from pathlib import Path
import shutil,json,hashlib
import numpy as np
import trimesh
ROOT=Path(__file__).resolve().parent
src=ROOT/'scad_output/spacer_1_width_1_height_9_mm_depth_slotted_extra'
name='spacer_1_width_1_height_14_mm_depth_slotted_extra'
dst=ROOT/'scad_output'/name;dst.mkdir(parents=True,exist_ok=True)
m=trimesh.load(src/'3dpr.stl',force='mesh')
assert m.is_watertight
old_volume=m.volume; old_xy=m.bounds[:,:2].copy()
m.apply_scale([1,1,14/9])
assert m.is_watertight and np.allclose(m.bounds[:,:2],old_xy)
assert abs(m.extents[2]-14)<1e-6
assert abs(m.volume/old_volume-14/9)<1e-6
m.export(dst/'3dpr.stl')
scad=(src/'3dpr.scad').read_text().replace('cylinder(h = 9,','cylinder(h = 14,').replace('size = [5, 20, 9]','size = [5, 20, 14]')
(dst/'3dpr.scad').write_text('// 14 mm axial variant of the original 9 mm slotted cover.\n'+scad)
catalogue=ROOT/'parts'/('project_github_oomlout_three_d_printing_filament_storage_kallax_'+name)
catalogue.mkdir(parents=True,exist_ok=True)
for f in ('3dpr.stl','3dpr.scad'):shutil.copy2(dst/f,catalogue/f)
meta={'source':(src/'3dpr.stl').relative_to(ROOT).as_posix(),'source_sha256':hashlib.sha256((src/'3dpr.stl').read_bytes()).hexdigest(),
      'length_mm':14,'derived_by':'axial scaling of constant-section 9 mm source; cross-section unchanged',
      'watertight':bool(m.is_watertight),'bounds_mm':m.bounds.tolist(),'quantity_per_cell':4}
(catalogue/'derivation.json').write_text(json.dumps(meta,indent=2))
(catalogue/'readme.md').write_text('# Slotted end cover - 14 mm\n\nDerived from the existing 9 mm slotted spacer without changing its cross-section.\nPrint four per complete cell. Rebuild with `python make_adjustment_cover.py`.\n\nFor the nominal 335 mm stack: 267.01 mm long sleeves + 36 mm side frames + 18 mm coupling housing + 14 mm cover = 335.01 mm.\n')
print(json.dumps(meta,indent=2))
