# KALLAX presentation package

Revision 3, 6 November 2026. Agent handoff and build notes. Published instructions are in the root README and assembly PDF.

Revision 3 combines printed parts and hardware in one BOM, adds verified MD5 alpha links and shortens the published copy. [source-notes.json](source-notes.json) retains the full draft. [scripts/revise_text.py](scripts/revise_text.py) applies the final editorial pass after configuration. Geometry is unchanged from revision 2.

**AI-generated documentation.** The CAD illustrations, section drawing, instructions and scripts were created with AI assistance and may contain mistakes. The project has not been physically assembled or load-tested as part of this work.

## Published files

- [Assembly guide](assembly-guide.pdf), seven pages.
- [Parts list](parts.csv), quantities for one and two cells.
- [Root README](../readme.md), illustrated assembly and installation instructions with OOMP links.
- [Published images](images), including the individual guide pages and end-section drawing. Each carries an AI notice.
- [Research notes](research.md), source links and style decisions.
- [Assembly data](project.json), the reviewed BOM, specifications, links and dimensional stack.

![AI-generated technical manual overview](images/guide-01.png)

## Assembly revision

Each cell has four short frames and four tall frames. The two holders are independent and each has two 300 mm M6 rods. Each rail has one fixed-end M6 nut, one 18 mm coupling nut, one M6 x 25 fully threaded hex-head bolt and one additional M6 nut retaining that bolt against the final frame.

The retaining nut is on the inside of the final frame. Its 7 mm full-hex cover occupies the last 7 mm before the frame and encloses the nominal 5 mm nut plus 2 mm of adjacent thread. The slotted cover between that cover and the coupling is now 7 mm. Both covers are existing production parts. The previous 14 mm cover is superseded for this assembly; it is retained as historical source geometry, not listed in the active BOM.

The final frame is reversed so its hex recess faces outward. The fixed-end nut and bolt head sit inside the respective outer pockets. Set the bolt length before tightening its retaining nut; the locked assembly is not a turnbuckle.

## Dimensions and evidence

| Item | Value or status |
| --- | --- |
| Printed parts per cell | 32 |
| Purchased hardware per cell | 20 pieces |
| Nominal width | 335.01 mm |
| Source sleeve total | 99.67 + 67.67 + 99.67 = 267.01 mm |
| Side-frame total | 4 x 9 = 36 mm |
| End covers and housing | 18 + 7 + 7 = 32 mm |
| Bolt length | 25 mm under head |
| Nominal engagement | Rod 5.99 mm; bolt 7 mm |
| Nominal clearance between tips | 5.01 mm |
| Source geometry | Existing STL parts imported at millimetre scale |
| OOMP hardware identity | Nut, coupling and full-thread hex-head set-screw entries checked |
| Exact OOMP 300 mm rod record | Not verified; cut stock is specified directly |
| Furniture opening | 335 mm assumed, not measured |
| Physical fit, snap fit and load capacity | Untested |

The nominal span is not a guaranteed clearance fit. Measure the actual cabinet and hardware. Thread engagement values exclude losses from chamfers and thread runout. The source hex pockets are 5 mm deep; the hardware illustration assumes a 4 mm bolt head and 5 mm ordinary nuts.

The cabinet and filament rolls are illustrative geometry. The 4 x 4 shell is 1470 x 1470 x 390 mm; IKEA's current page gives a 1465 mm product height. The source model was retained as a setting, not presented as a furniture manufacturing drawing. Front reels are generic 200 x 60 mm, rear refills 200 x 58 mm, with five at 62 mm centres. Black holder materials override the default OOBB palette; teal, yellow and black remain on the illustrated filament.

## Rebuild

Run these commands from the project root. The Python scripts resolve paths from their own locations, so absolute script paths also work from another working directory.

```powershell
# Rebuild text, PDF, CSV, labelled images and copies beside active catalogue STLs.
python presentation/scripts/build.py

# Rebuild all seven CAD views first, then the presentation package.
python presentation/scripts/build.py --render --blender 'C:/Program Files/Blender Foundation/Blender 5.2/blender.exe'

# Read-only checks of actual saved scene counts and recessed hardware positions.
& 'C:/Program Files/Blender Foundation/Blender 5.2/blender.exe' --background --python-exit-code 1 --python presentation/scripts/audit_scene.py

# Validate local README links, images, quantities and PDF text bounds.
python presentation/scripts/lib/validate_presentation.py .
```

Requirements: Python with ReportLab, Pillow and PyMuPDF; Blender 5.2 for CAD rendering. The CAD geometry audit runs in Blender. Source-mesh validation additionally uses trimesh and NumPy. See [requirements.txt](requirements.txt).

`scripts/configure.py` records the reviewed assembly and writes `project.json`. It is not run during a normal rebuild. Edit the manifest directly or update and run this configuration script deliberately. The renderer asserts its supported dimensions; a different axial stack needs corresponding transform and section-drawing updates.

The reusable helpers are vendored in `scripts/lib/` and the README template in `templates/`. Their source is the base OOBB repository's `presentation/` folder. Copy updated helpers deliberately and review the result; project builds do not depend on an absolute path to that repository.

## Validation and source records

- [Package validation](qa/validation.json): links, quantities, published images and PDF bounds.
- [Scene audit](qa/scene-audit.json): expected repeated parts and fastener positions in the saved scenes.
- [Source mesh audit](qa/source-meshes.json): exact STL hashes, extents and watertight status.
- [Hardware source checks](qa/hardware-links.json): inspected public records and dimensional reference.
- [Visual contact sheet](qa/contact-sheet.png): all current guide pages.

Review the full-size page PNGs as well as the contact sheet. These checks are digital, not a successful assembly test. Printed material selection, print settings, tightening torque, hardware access and load capacity are not established here.

## File ownership and older outputs

`../render_kallax.py` is the current CAD renderer. `scripts/build.py` controls page composition and published outputs. The root `make_visual_guide.py` is a compatibility entry point for the current builder. The old PDF download path under `output/pdf/` is updated to the current guide.

The previous `renders/` outputs are historical and should not be used in a new README. The active `parts/` folders receive the current assembled, exploded, parts-list, assembly and end-detail PNGs. The old 14 mm variant is not regenerated by this workflow. No source production STL was changed in revision 2.
