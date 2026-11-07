<!-- oobb-presentation:start -->
# KALLAX filament holders

Two independent printed holders support five narrow filament reels at the front of one KALLAX cell and five strapped, spool-free refills at the rear. All printed parts are black.

**AI-generated documentation.** The images, assembly instructions and dimension calculations were generated with AI assistance. They may contain mistakes. Check the CAD, hardware and physical fit before building. This is a CAD assembly study. It has not been physically assembled or load-tested.

![AI-generated CAD render: five front reels and five raised rear refills in one KALLAX cell](presentation/images/cell.png)

[Assembly guide (PDF)](presentation/assembly-guide.pdf) · [Parts list (CSV)](presentation/parts.csv) · [Presentation sources](presentation/README.md)

## Configuration

One cell uses four short side frames at the front and four tall side frames at the rear. Each holder has two rails, each built around one 300 mm M6 threaded rod. The front and rear holders do not connect. Two populated cells in a 4 x 4 unit require twice the quantities listed for one cell.

The illustrated internal opening is nominally 335 mm wide. Measure the actual opening before fitting. The generic front reels are 200 mm in diameter and 60 mm wide; five at 62 mm centres occupy 308 mm. The rear refills are 200 mm in diameter and 58 mm wide. These are dimensional examples, not verified product compatibility.

![AI-generated CAD render: two populated cells in a 4 by 4 KALLAX shelving unit](presentation/images/cabinet.png)

## Parts

Quantities are for one complete cell: one short holder and one tall holder. There are 32 printed parts and 20 purchased hardware pieces per cell. Print all holder parts in black. The 14 mm cover from the previous revision is superseded by a 7 mm nut cover plus a 7 mm slotted cover.

### Printed parts

| Ref. | Part | Specification | Per cell | Two cells |
| --- | --- | --- | ---: | ---: |
| P1 | [Short side frame](parts/project_github_oomlout_three_d_printing_filament_storage_kallax_side_10_width_3_height_9_mm_depth_short_extra/3dpr.stl) | 149 x 44 x 9 mm | 4 | 8 |
| P2 | [Tall side frame](parts/project_github_oomlout_three_d_printing_filament_storage_kallax_side_10_width_8_height_9_mm_depth_short_extra/3dpr.stl) | 149 x 119 x 9 mm | 4 | 8 |
| P3 | [Long sleeve](parts/project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_99_67_mm_depth_one_end_nut_extra/3dpr.stl) | 99.67 mm long; one-end hex pocket | 8 | 16 |
| P4 | [Centre sleeve](parts/project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_67_67_mm_depth_one_end_nut_extra/3dpr.stl) | 67.67 mm long; one-end hex pocket | 4 | 8 |
| P5 | [Coupling housing](parts/project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_18_mm_depth_full_nut_extra/3dpr.stl) | 18 mm long; full hex bore | 4 | 8 |
| P6 | [Retaining nut cover](parts/project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_7_mm_depth_full_nut_extra/3dpr.stl) | 7 mm long; full hex bore | 4 | 8 |
| P7 | [Slotted cover](parts/project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_7_mm_depth_slotted_extra/3dpr.stl) | 7 mm long; open slot | 4 | 8 |

### Hardware

| Ref. | Part | Specification | Per cell | Two cells |
| --- | --- | --- | ---: | ---: |
| H1 | M6 threaded rod | 300 mm cut length; M6 x 1.0 | 4 | 8 |
| H2 | [M6 hex nut](https://github.com/oomlout/oomlout_oomp_version_1_messy/tree/main/parts/hardware_nut_m6) | 10 mm AF; 5 mm nominal thickness | 8 | 16 |
| H3 | [M6 coupling nut](https://github.com/oomlout/oomlout_oomp_version_1_messy/tree/main/parts/hardware_nut_m6_coupling) | DIN 6334; 18 mm long; 10 mm AF | 4 | 8 |
| H4 | [M6 x 25 hex-head bolt, fully threaded](https://github.com/oomlout/oomp_hardware_bolt_version_5/tree/main/parts/hardware_set_screw_m6_25_mm_length) | 25 mm under head; M6 x 1.0; DIN 933 | 4 | 8 |

Each rail uses two ordinary M6 nuts: one captive nut at the fixed end and one nut retaining the adjustment bolt against the final frame. It still uses only one coupling nut.

OOMP calls the fully threaded hex-head fastener a **set screw**. Use the linked `hardware_set_screw_m6_25_mm_length` entry, not a headless grub screw or the partly threaded `hardware_bolt_m6_25_mm_length`. An exact OOMP entry for the 300 mm rod was not found in the checked catalogues; the rod is specified directly rather than linked to an unverified ID. Catalogue identity does not verify the dimensions of hardware in hand.

## Preparation

Measure the cell width at both rail heights. Check the recesses against the actual nuts and bolt heads. Cut four M6 rods to 300 mm and deburr both ends; confirm that a nut runs freely along each thread. Prepare a ruler or calipers and a 10 mm spanner. Use the project print files; material, infill and print strength have not been validated by this presentation.

## Assembly

![AI-generated CAD render: exploded short holder showing four side frames and two threaded rails](presentation/images/exploded.png)

1. Seat a fixed-end M6 nut in each outer hex recess of the first side frame. Thread one 300 mm rod into each nut and leave the rod end flush with the outer face.

2. On both rods, add a 99.67 mm sleeve, the second frame, a 67.67 mm sleeve, the third frame, then the second 99.67 mm sleeve. Orient the final long sleeve with its hex pocket toward the coupling end.

3. Insert one 18 mm M6 coupling nut into each 18 mm full-hex housing. Thread each coupling onto its rod. The nominal model places the coupling from 294.01 to 312.01 mm, giving approximately 6 mm of rod engagement.

4. Turn the fourth frame so its bolt-head recesses face outward. Put an M6 x 25 fully threaded hex-head bolt through each recess. Thread one retaining M6 nut onto each bolt on the inside of the frame, leaving it loose. Slide a 7 mm full-hex cover onto each bolt and over its retaining nut before engaging the bolt in the coupling.

5. Thread each bolt into its coupling and set the overall width before clamping the retaining nut. Temporarily withdraw the head from its pocket if it must turn. Seat both hex heads fully in the outward-facing recesses. Slide each nut cover toward the coupling to expose the retaining nut; tighten the nut against the inner face of the final frame, then slide the cover back over it. Do not use the assembly to force the cabinet sides apart.

6. Clip the 7 mm slotted cover over the remaining exposed thread between the coupling housing and retaining-nut cover. Check that both fixed nuts and bolt heads remain inside the frame recesses. Repeat with four tall frames for the rear holder.

## Adjustable end

![AI-generated engineering section: one coupling, 7 mm clip, retaining nut in a 7 mm hex cover and recessed bolt head](presentation/images/end-section.png)

The final end has a retaining nut directly against the inner face of the last frame. Its 7 mm full-hex cover encloses the nominal 5 mm nut and 2 mm of adjacent thread. The remaining slotted cover is 7 mm long. The bolt remains M6 x 25 mm.

At the nominal setting, the coupling ends at 312.01 mm; the clip occupies 312.01-319.01 mm; the hex cover occupies 319.01-326.01 mm; the retaining nut occupies 321.01-326.01 mm. The final frame occupies 326.01-335.01 mm. Its outer 5 mm pocket contains the bolt head, leaving the retaining nut and head bearing against opposite sides of the frame web.

To change the setting, remove the slotted cover, slide the hex cover away, loosen the retaining nut and release the bolt head from its recess before turning the bolt. Reseat and retain it afterwards. Do not assume the locked assembly adjusts by turning the coupling alone.

## Installation

1. Place the tall holder at the back of the cell and the short holder at the front. Both sets of feet rest on the shelf. The model uses 187 mm between row centres and a 75 mm difference in rail height.

2. Check the fit without filament. Confirm that each frame sits flat, each nut and head is seated, and the cabinet is not being spread by the adjustment bolts. The nominal 335.01 mm CAD span is not a guaranteed clearance fit in a 335 mm opening.

3. Load the rear refills with their retaining straps fitted, then load the front reels. Check the actual roll widths and diameters; stop if rolls interfere or a holder rocks or deforms.

4. For a second cell, repeat the complete assembly. Follow the furniture manufacturer's installation instructions for the KALLAX unit itself.

## Dimensions and verification

The axial stack per rail is:

`4 x 9 + 2 x 99.67 + 67.67 + 18 + 7 + 7 = 335.01 mm`

For another measured opening, the calculated slotted cover length is `opening - 328.01 mm`, assuming the other parts and seating positions are unchanged. Recheck bolt engagement and recess fit before changing it.

The seated bolt bearing face is at 330.01 mm. A 25 mm bolt ends at 305.01 mm, giving 7 mm of nominal engagement in the coupling and 5.01 mm clearance to the rod tip. Coupling chamfers and thread runout reduce effective full-thread engagement. The drawing uses a nominal 4 mm bolt head inside a 5 mm pocket; check the purchased head height.

Checked in the digital model: part counts, mesh dimensions, retaining-nut position, recessed head and fixed-nut positions, nominal axial stack and local file links. Not checked physically: print tolerances, snap fit, assembly access, actual reel compatibility, cabinet opening, material strength or load capacity.

The supplied 7 mm nut cover and slotted cover are existing project parts. No production STL was changed for this revision. The thread helices and purchased hardware in the renders are simplified illustrations; the printed parts use the source STL geometry.

## Files and sources

- [Production print files](scad_output) and [catalogue parts](parts).
- [OOMP M6 nut](https://github.com/oomlout/oomlout_oomp_version_1_messy/tree/main/parts/hardware_nut_m6) and [M6 coupling nut](https://github.com/oomlout/oomlout_oomp_version_1_messy/tree/main/parts/hardware_nut_m6_coupling).
- [OOMP M6 x 25 fully threaded hex-head set screw](https://github.com/oomlout/oomp_hardware_bolt_version_5/tree/main/parts/hardware_set_screw_m6_25_mm_length).
- [Accu M6 DIN 6334 coupling dimensions](https://www.accu.co.uk/hexagonal-stud-connector-nuts/62290-HTBN-M6-A2): 18 mm long and 10 mm across flats.
- [IKEA KALLAX 4 x 4 unit](https://www.ikea.com/gb/en/p/kallax-shelving-unit-white-30275861/): external furniture reference. The 335 mm opening is a modelling assumption.
- [Research and presentation decisions](presentation/research.md). Hardware catalogue links checked 6 November 2026.

The presentation workflow, assumptions and rebuild commands are documented in [presentation/README.md](presentation/README.md).
<!-- oobb-presentation:end -->

# Three D Printing Filament Storage Kallax Holder


Three D Printing Filament Storage Kallax Holder  
  





















## oolc_production
Laser cutting production files can be found in the [oolc_production](oolc_production) folder.

## 3d printing files
3d printing files can be found in the [scad_output](scad_output) folder.

