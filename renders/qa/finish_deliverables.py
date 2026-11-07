from pathlib import Path
import csv,json,shutil
import fitz,trimesh,numpy as np
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[2]
rows=list(csv.DictReader((root/'renders/parts_manifest.csv').open()))
printed=[r for r in rows if r['source_stl'].endswith('.stl')]
assert sum(int(r['quantity_per_cell']) for r in printed)==28
for r in printed:
    folder=(root/r['source_stl']).parent
    assert folder.is_relative_to(root/'parts') and (folder/'3dpr.stl').exists()
    page='guide-3.png' if 'side frame' in r['part'] else 'guide-4.png'
    for src,name in [(page,'assembly_guide.png'),('guide-5.png','parts_list.png'),('guide-7.png','end_detail.png')]:
        shutil.copy2(root/'renders/guide_pages'/src,folder/name)
doc=fitz.open(root/'output/pdf/kallax_filament_visual_assembly_guide.pdf')
assert len(doc)==7
for page in doc:
    assert all(w[0]>=0 and w[1]>=0 and w[2]<=900 and w[3]<=675 for w in page.get_text('words'))
mesh=trimesh.load(root/'scad_output/spacer_1_width_1_height_14_mm_depth_slotted_extra/3dpr.stl')
scad_mesh=trimesh.load(root/'renders/qa/cover_14_from_scad.stl')
assert mesh.is_watertight and scad_mesh.is_watertight
assert np.allclose(mesh.bounds,scad_mesh.bounds,atol=.0002)
assert np.isclose(mesh.volume,scad_mesh.volume,rtol=.0001)
# Superseded previews made by this task are retained only in QA.
obsolete=root/'parts/project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_8_mm_depth_full_nut_extra'
for name in ('assembly_guide.png','parts_list.png','presentation_assembled.png','presentation_exploded.png'):
    p=obsolete/name
    if p.exists():p.replace(root/'renders/qa'/('obsolete_8mm_'+name))
for p in (root/'renders/guide_pages').glob('review-*.png'):
    p.replace(root/'renders/qa'/('previous_'+p.name))
sheet=Image.new('RGB',(1600,1600),'white');draw=ImageDraw.Draw(sheet)
for i,shot in enumerate(('cell','cabinet','loaded','empty','rail','exploded','adjust')):
    im=Image.open(root/'renders/raw'/f'{shot}.png');im.thumbnail((790,370))
    x=i%2*800;y=i//2*400
    sheet.paste(im,(x+(800-im.width)//2,y+25));draw.text((x+15,y+5),shot,fill='black')
sheet.save(root/'renders/qa/final_contact.png')
result={'pdf_pages':7,'printed_parts_per_cell':28,'cover_watertight':True,
        'cover_scad_matches_stl':True,'cover_length_mm':float(mesh.extents[2]),
        'nominal_printed_width_mm':267.01+36+18+14,'bolt_under_head_mm':25}
(root/'renders/qa/final_validation.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
