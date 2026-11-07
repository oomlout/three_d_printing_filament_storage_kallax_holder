"""Write the reviewed assembly data. Run explicitly when the design changes.
The normal build reads project.json; it does not run this configuration script.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
PREFIX='project_github_oomlout_three_d_printing_filament_storage_kallax_'
printed=[]
for ref,name,qty,spec,part in [
 ('P1','Short side frame',4,'149 x 44 x 9 mm','side_10_width_3_height_9_mm_depth_short_extra'),
 ('P2','Tall side frame',4,'149 x 119 x 9 mm','side_10_width_8_height_9_mm_depth_short_extra'),
 ('P3','Long sleeve',8,'99.67 mm long; one-end hex pocket','spacer_1_width_1_height_99_67_mm_depth_one_end_nut_extra'),
 ('P4','Centre sleeve',4,'67.67 mm long; one-end hex pocket','spacer_1_width_1_height_67_67_mm_depth_one_end_nut_extra'),
 ('P5','Coupling housing',4,'18 mm long; full hex bore','spacer_1_width_1_height_18_mm_depth_full_nut_extra'),
 ('P6','Retaining nut cover',4,'7 mm long; full hex bore','spacer_1_width_1_height_7_mm_depth_full_nut_extra'),
 ('P7','Slotted cover',4,'7 mm long; open slot','spacer_1_width_1_height_7_mm_depth_slotted_extra')]:
    printed.append(dict(ref=ref,name=name,quantity=qty,spec=spec,part=part,stl=f'parts/{PREFIX}{part}/3dpr.stl',verification='Existing source STL; physical fit untested'))
old='https://github.com/oomlout/oomlout_oomp_version_1_messy/tree/main/parts/'
bolt='https://github.com/oomlout/oomp_hardware_bolt_version_5/tree/main/parts/hardware_set_screw_m6_25_mm_length'
hardware=[
 dict(ref='H1',name='M6 threaded rod',quantity=4,spec='300 mm cut length; M6 x 1.0',url='',oomp_id=None,verification='Exact OOMP rod entry not found; specify and cut stock'),
 dict(ref='H2',name='M6 hex nut',quantity=8,spec='10 mm AF; 5 mm nominal thickness',url=old+'hardware_nut_m6',oomp_id='hardware_nut_m6',verification='OOMP identity verified 2026-11-06; actual thickness to be checked'),
 dict(ref='H3',name='M6 coupling nut',quantity=4,spec='DIN 6334; 18 mm long; 10 mm AF',url=old+'hardware_nut_m6_coupling',oomp_id='hardware_nut_m6_coupling',verification='OOMP identity verified 2026-11-06; 18 mm dimensions from Accu'),
 dict(ref='H4',name='M6 x 25 hex-head bolt, fully threaded',quantity=4,spec='25 mm under head; M6 x 1.0; DIN 933',url=bolt,oomp_id='hardware_set_screw_m6_25_mm_length',verification='OOMP full-thread hex-head identity verified 2026-11-06; no grub screw')]
data={
 'schema_version':1,'revision':'2','date':'2026-11-06','title':'KALLAX filament holders',
 'readme_filename':'readme.md','quantity_columns':['Per cell','Two cells'],'printed_parts':printed,'hardware':hardware,
 'geometry':{'opening_nominal_mm':335,'span_mm':335.01,'rod_mm':300,'bolt_mm':25,'coupler_mm':18,'clip_mm':7,'nut_cover_mm':7,
             'rod_engagement_mm':5.99,'bolt_engagement_mm':7,'tip_gap_mm':5.01,'printed_count':32,
             'axial_stack':[['Frame 1',0,9],['Long sleeve',9,108.67],['Frame 2',108.67,117.67],['Centre sleeve',117.67,185.34],['Frame 3',185.34,194.34],['Long sleeve',194.34,294.01],['Coupling housing',294.01,312.01],['Slotted cover',312.01,319.01],['Retaining nut cover',319.01,326.01],['Frame 4',326.01,335.01]],
             'hardware_intervals':{'fixed_nut':[0,5],'rod':[0,300],'coupling':[294.01,312.01],'retaining_nut':[321.01,326.01],'bolt_shank':[305.01,330.01],'bolt_head':[330.01,334.01]}},
 'readme':{
 'summary':'Two independent printed holders support five narrow filament reels at the front of one KALLAX cell and five strapped, spool-free refills at the rear. All printed parts are black.',
 'validation_status':'This is a CAD assembly study. It has not been physically assembled or load-tested.',
 'hero_alt':'AI-generated CAD render: five front reels and five raised rear refills in one KALLAX cell',
 'hero_image':'cell.png',
 'configuration':'One cell uses four short side frames at the front and four tall side frames at the rear. Each holder has two rails, each built around one 300 mm M6 threaded rod. The front and rear holders do not connect. Two populated cells in a 4 x 4 unit require twice the quantities listed for one cell.\n\nThe illustrated internal opening is nominally 335 mm wide. Measure the actual opening before fitting. The generic front reels are 200 mm in diameter and 60 mm wide; five at 62 mm centres occupy 308 mm. The rear refills are 200 mm in diameter and 58 mm wide. These are dimensional examples, not verified product compatibility.',
 'configuration_alt':'AI-generated CAD render: two populated cells in a 4 by 4 KALLAX shelving unit',
 'configuration_image':'cabinet.png',
 'quantity_basis':'one complete cell: one short holder and one tall holder',
 'quantity_note':'There are 32 printed parts and 20 purchased hardware pieces per cell. Print all holder parts in black. The 14 mm cover from the previous revision is superseded by a 7 mm nut cover plus a 7 mm slotted cover.',
 'hardware_notes':'Each rail uses two ordinary M6 nuts: one captive nut at the fixed end and one nut retaining the adjustment bolt against the final frame. It still uses only one coupling nut.\n\nOOMP calls the fully threaded hex-head fastener a **set screw**. Use the linked `hardware_set_screw_m6_25_mm_length` entry, not a headless grub screw or the partly threaded `hardware_bolt_m6_25_mm_length`. An exact OOMP entry for the 300 mm rod was not found in the checked catalogues; the rod is specified directly rather than linked to an unverified ID. Catalogue identity does not verify the dimensions of hardware in hand.',
 'preparation':'Measure the cell width at both rail heights. Check the recesses against the actual nuts and bolt heads. Cut four M6 rods to 300 mm and deburr both ends; confirm that a nut runs freely along each thread. Prepare a ruler or calipers and a 10 mm spanner. Use the project print files; material, infill and print strength have not been validated by this presentation.',
 'assembly_alt':'AI-generated CAD render: exploded short holder showing four side frames and two threaded rails',
 'assembly_image':'exploded.png',
 'assembly_steps':[
 'Seat a fixed-end M6 nut in each outer hex recess of the first side frame. Thread one 300 mm rod into each nut and leave the rod end flush with the outer face.',
 'On both rods, add a 99.67 mm sleeve, the second frame, a 67.67 mm sleeve, the third frame, then the second 99.67 mm sleeve. Orient the final long sleeve with its hex pocket toward the coupling end.',
 'Insert one 18 mm M6 coupling nut into each 18 mm full-hex housing. Thread each coupling onto its rod. The nominal model places the coupling from 294.01 to 312.01 mm, giving approximately 6 mm of rod engagement.',
 'Turn the fourth frame so its bolt-head recesses face outward. Put an M6 x 25 fully threaded hex-head bolt through each recess. Thread one retaining M6 nut onto each bolt on the inside of the frame, leaving it loose. Slide a 7 mm full-hex cover onto each bolt and over its retaining nut before engaging the bolt in the coupling.',
 'Thread each bolt into its coupling and set the overall width before clamping the retaining nut. Temporarily withdraw the head from its pocket if it must turn. Seat both hex heads fully in the outward-facing recesses. Slide each nut cover toward the coupling to expose the retaining nut; tighten the nut against the inner face of the final frame, then slide the cover back over it. Do not use the assembly to force the cabinet sides apart.',
 'Clip the 7 mm slotted cover over the remaining exposed thread between the coupling housing and retaining-nut cover. Check that both fixed nuts and bolt heads remain inside the frame recesses. Repeat with four tall frames for the rear holder.'
 ],
 'detail_alt':'AI-generated engineering section: one coupling, 7 mm clip, retaining nut in a 7 mm hex cover and recessed bolt head',
 'detail_image':'end-section.png',
 'adjustment':'The final end has a retaining nut directly against the inner face of the last frame. Its 7 mm full-hex cover encloses the nominal 5 mm nut and 2 mm of adjacent thread. The remaining slotted cover is 7 mm long. The bolt remains M6 x 25 mm.\n\nAt the nominal setting, the coupling ends at 312.01 mm; the clip occupies 312.01-319.01 mm; the hex cover occupies 319.01-326.01 mm; the retaining nut occupies 321.01-326.01 mm. The final frame occupies 326.01-335.01 mm. Its outer 5 mm pocket contains the bolt head, leaving the retaining nut and head bearing against opposite sides of the frame web.\n\nTo change the setting, remove the slotted cover, slide the hex cover away, loosen the retaining nut and release the bolt head from its recess before turning the bolt. Reseat and retain it afterwards. Do not assume the locked assembly adjusts by turning the coupling alone.',
 'installation_steps':[
 'Place the tall holder at the back of the cell and the short holder at the front. Both sets of feet rest on the shelf. The model uses 187 mm between row centres and a 75 mm difference in rail height.',
 'Check the fit without filament. Confirm that each frame sits flat, each nut and head is seated, and the cabinet is not being spread by the adjustment bolts. The nominal 335.01 mm CAD span is not a guaranteed clearance fit in a 335 mm opening.',
 'Load the rear refills with their retaining straps fitted, then load the front reels. Check the actual roll widths and diameters; stop if rolls interfere or a holder rocks or deforms.',
 'For a second cell, repeat the complete assembly. Follow the furniture manufacturer\'s installation instructions for the KALLAX unit itself.'
 ],
 'dimensions':'The axial stack per rail is:\n\n`4 x 9 + 2 x 99.67 + 67.67 + 18 + 7 + 7 = 335.01 mm`\n\nFor another measured opening, the calculated slotted cover length is `opening - 328.01 mm`, assuming the other parts and seating positions are unchanged. Recheck bolt engagement and recess fit before changing it.\n\nThe seated bolt bearing face is at 330.01 mm. A 25 mm bolt ends at 305.01 mm, giving 7 mm of nominal engagement in the coupling and 5.01 mm clearance to the rod tip. Coupling chamfers and thread runout reduce effective full-thread engagement. The drawing uses a nominal 4 mm bolt head inside a 5 mm pocket; check the purchased head height.',
 'verification':'Checked in the digital model: part counts, mesh dimensions, retaining-nut position, recessed head and fixed-nut positions, nominal axial stack and local file links. Not checked physically: print tolerances, snap fit, assembly access, actual reel compatibility, cabinet opening, material strength or load capacity.\n\nThe supplied 7 mm nut cover and slotted cover are existing project parts. No production STL was changed for this revision. The thread helices and purchased hardware in the renders are simplified illustrations; the printed parts use the source STL geometry.',
 'sources':'- [Production print files](scad_output) and [catalogue parts](parts).\n- [OOMP M6 nut]('+old+'hardware_nut_m6) and [M6 coupling nut]('+old+'hardware_nut_m6_coupling).\n- [OOMP M6 x 25 fully threaded hex-head set screw]('+bolt+').\n- [Accu M6 DIN 6334 coupling dimensions](https://www.accu.co.uk/hexagonal-stud-connector-nuts/62290-HTBN-M6-A2): 18 mm long and 10 mm across flats.\n- [IKEA KALLAX 4 x 4 unit](https://www.ikea.com/gb/en/p/kallax-shelving-unit-white-30275861/): external furniture reference. The 335 mm opening is a modelling assumption.\n- [Research and presentation decisions](presentation/research.md). Hardware catalogue links checked 6 November 2026.'
 }}
(ROOT/'presentation/project.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
print('Wrote presentation/project.json')
import runpy
runpy.run_path(str(ROOT/'presentation/scripts/revise_text.py'),run_name='__main__')
