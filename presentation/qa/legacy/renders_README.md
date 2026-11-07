# KALLAX filament holder visuals

Updated to the user's four-frame assembly. Each holder has four side frames on two rods: four short frames at the front and four tall frames at the rear. The two holders are independent.

## Deliverables

- [Single cell](raw/cell.png)
- [Two populated cells in a 4 x 4 KALLAX](raw/cabinet.png)
- [Loaded holders outside the shelf](raw/loaded.png)
- [Four-frame holders, unloaded](raw/empty.png)
- [Exploded rail hardware](raw/rail.png)
- [Exploded short holder](raw/exploded.png)
- [Adjustable-end detail](raw/adjust.png)
- [Seven-page visual and assembly PDF](../output/pdf/kallax_filament_visual_assembly_guide.pdf)
- [Guide pages as PNGs](guide_pages/)
- [Exact STL manifest and quantities](parts_manifest.csv)
- [Editable Blender scenes](scenes/)

## Confirmed arrangement

Four M6 x 300 mm rods per cell. Each rail has a captive fixed-end nut, ONE coupling nut and a bolt to adjust the full width. Five complete narrow non-Bambu reels occupy the front row, with spool-free refills behind. All printed parts are black; filament colours are OOBB turquoise, sunflower yellow and black.

## Calculated recessed end assembly

The standard M6 DIN 6334 coupling is 18 mm long and 10 mm across flats: [Accu specification](https://www.accu.co.uk/hexagonal-stud-connector-nuts/62290-HTBN-M6-A2). Use a fully threaded **M6 x 25 mm hex-head bolt** for the nominal 335 mm cell. Both the fixed nut and bolt head sit inside outward-facing recesses. The final side frame is reversed to put its recess on the outside.

Sequence: frame / 99.67 sleeve / frame / 67.67 sleeve / frame / 99.67 sleeve / 18 mm nut housing / 14 mm slotted cover / final frame. All lengths are millimetres.

The existing 18 mm full-hex-bore print encloses the entire coupling. The 14 mm cover is a new axial variant of the original 9 mm slotted part, preserving its cross-section. Its slot faces down in the assembled renders. Original parts are unchanged.

Cover length = opening - (267.01 mm sleeves + 36 mm frames + 18 mm nut housing). For a nominal 335 mm cell this gives 13.99 mm, rounded to a 14 mm printable cover. Total stack is 335.01 mm. The 0.01 mm difference is rounding; measure the actual opening. A 9 mm cover leaves about 5 mm uncovered.

Axial coordinates measured from the fixed-end outer face:

| Item | Start mm | End mm |
|---|---:|---:|
| Frame 1 | 0 | 9 |
| Sleeve 1 | 9 | 108.67 |
| Frame 2 | 108.67 | 117.67 |
| Sleeve 2 | 117.67 | 185.34 |
| Frame 3 | 185.34 | 194.34 |
| Sleeve 3 | 194.34 | 294.01 |
| Coupling nut and housing | 294.01 | 312.01 |
| Slotted cover | 312.01 | 326.01 |
| Frame 4 | 326.01 | 335.01 |
| Captive fixed nut | 0 | 5 |
| Threaded rod | 0 | 300 |
| Bolt shank, M6 x 25 | 305.01 | 330.01 |
| Bolt head, nominal 4 mm | 330.01 | 334.01 |
| Bolt-head recess | 330.01 | 335.01 |

The 25 mm bolt has 7 mm geometric coupling engagement and 5.01 mm clearance to the rod tip. Rod engagement is 5.99 mm, nominally 6 mm. A 20 mm bolt would engage only 2 mm; a 30 mm bolt would leave only 0.01 mm between tips. These are geometric calculations, not a load test. Check actual dimensions, thread-end chamfers and fit.

## Parts per cell

4 short frames; 4 tall frames; 8 x 99.67 mm sleeves; 4 x 67.67 mm sleeves; 4 x 18 mm nut housings; 4 x 14 mm slotted covers; 4 x 300 mm rods; 4 captive M6 nuts; 4 M6 coupling nuts; 4 M6 x 25 fully threaded hex-head bolts. Total: 28 printed pieces per cell. Double the quantities for the two cells shown.

Earlier two-frame and projecting-bolt reconstructions are superseded. The 8 mm collar arrangement is not used.

## New printable cover

[14 mm slotted cover STL](../parts/project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_14_mm_depth_slotted_extra/3dpr.stl)

Regenerate with `python make_adjustment_cover.py`. The constant-section 9 mm source is extended axially; XY dimensions and slot profile are unchanged. The new mesh is watertight. Source SCAD and derivation metadata are saved beside it.

## Geometry and presentation

Side frames are imported directly from production STLs. Short frame bounds: 149 x 43.9802 x 9 mm; tall: 149 x 118.9802 x 9 mm. The guide rounds heights to 44 and 119 mm. Rails are 135 mm apart in depth, nominally 37 and 112 mm above the shelf.

Illustrated front reels are generic 200 mm diameter x 60 mm wide, at 62 mm centres: five occupy 308 mm. Rear refills are 200 mm diameter x 58 mm wide with retaining straps, no hub and no flanges. Their centres are 187 mm behind and 75 mm higher than the front row. This is a visual fit study, not a brand-specific fit guarantee.

The 4 x 4 shelf envelope is 1470 x 1470 x 390 mm, based on [IKEA UK KALLAX](https://www.ikea.com/gb/en/p/kallax-shelving-unit-white-30275861/). Internal openings of 335 mm, 16 mm internal dividers and 41 mm outer panels are modelling assumptions. The isolated cell is a cell study, not a dimensioned KALLAX 1 x 1 product model.

Presentation follows C:/gh/oomlout_oobb_version_5/RENDER_STYLE.md: orthographic views, soft studio lights, satin black print finish and steel hardware. The user's all-black instruction overrides the usual multicolour printed-part palette. Filament is turquoise #00B1B7, sunflower #FEC601 and black. Purchased hardware and threads are visualization geometry. Original STLs are unchanged; the 14 mm cover is a separate added variant.

## Rebuild

Run Blender in background with render_kallax.py and a shot argument after --. Shots: cell, cabinet, loaded, empty, rail, exploded, adjust. Then run export_render_anchors.py in Blender, followed by python make_visual_guide.py. Render the PDF pages with Poppler for visual review.

The generator copies presentation PNGs beside the corresponding production STLs in their actual parts catalogue folders. Guide PNGs are copied there after PDF rendering and visual QA.
