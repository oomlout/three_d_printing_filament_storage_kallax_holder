# Documentation build

Current standard: OOBB assembly style 4, adopted 19 November 2026.

Read the base repository's [assembly guide](../oomlout_oobb_version_5/ASSEMBLY_INSTRUCTIONS_GUIDE.md), [README guidelines](../oomlout_oobb_version_5/README_GUIDELINES.md) and [render style](../oomlout_oobb_version_5/RENDER_STYLE.md). The [wave-drive booklet](../oomlout_oobb_part_motor_gearbox_wave_drive_version_5/parts/oobb_part_motor_gearbox_wave_drive_version_5_12_to_1_reduction/assembly/assembly_instructions.pdf) is the reference. Existing KALLAX geometry and user corrections take precedence over reference mechanics.

## Build

```powershell
python working.py
python working.py --assembly-only
python working.py --no-renders
```

The first two commands render the current production STLs and rebuild the documents. They do not regenerate the original mechanical CAD. The last command checks mesh, renderer, staging and image hashes before reusing diagrams. It fails if geometry or staging changed. No command publishes to GitHub or runs an AI service.

The pipeline is `working_oomp_populate.py` -> `working_oomp.py` -> `working_scad.py` -> `components/kallax/`. Invoke `working.py` by absolute path from another directory if needed. The previous root automation launcher is preserved at `source_file/working_legacy.py`; it is historical, not a supported build command.

Dependencies: Python 3.12, Blender 5.2 on PATH, Pillow, ReportLab, PyMuPDF and svglib. Install Python dependencies from `components/kallax/requirements.txt`. Fonts use Segoe UI and Consolas on Windows, with Helvetica/Courier fallbacks. No dependence on the wave-drive checkout at runtime.

## Authoring

Edit `define_project_readme`, `define_assembly_card_style`, `define_assembly_book`, `define_assembly_part_labels` and `define_assembly_cards` in populate. Keep explicit dictionaries, `copy.deepcopy`, `kwargs.setdefault` and `**kwargs` forwarding. Edit `components/kallax/instances.py` only when the physical arrangement changes.

Twelve operations build the short holder, then the tall holder. The complete front holder remains in the rear-holder steps. Each new part has a named physical instance; the builder rejects duplicate additions, missing instances, quantity mismatches and more than four part types per panel. Step 13 is the finished pair and introduces no parts. Inventory: 32 printed pieces and 20 purchased pieces.

Public wording has two levels: concise actions in the version README and ASSEMBLY.md; pictorial panels contain only numbers, part names, quantities and hardware links. Keep the complete engineering rationale in source notes. After authoring, remove repeated explanations and unnecessary words.

## Deliverables

Active version: `parts/project_github_oomlout_three_d_printing_filament_storage_kallax_one_cell/`.

| File | Purpose |
| --- | --- |
| `README.md` | Design, printed-part and hardware tables, linked print files, assembly and installation |
| `ASSEMBLY.md` | Short written sequence with real 480 px thumbnails linking to panels |
| `assembly/assembly_instructions.pdf` | Eight landscape A4 pages in reading order |
| `assembly/assembly_instructions.html` | Self-contained offline viewer; no external scripts, fonts or image dependencies |
| `assembly/assembly_manifest.json` | Physical instances, steps, quantities, source and generator hashes, link provenance |
| `assembly/parts.csv` | Full printed and hardware BOM |
| `assembly/cards/`, `pages/`, `thumbnails/` | Individual panels, all PDF pages and GitHub thumbnails |
| `assembly/contact_sheet.png` | Whole-book review sheet |
| `assembly/validation.json` | Inventory, page geometry, typography and output checks |
| `assembly/review.json` | Dated visual/browser review tied to PDF and HTML hashes |
| `assembly/render/` | Raw CAD images, editable Blender scenes, render log and cache hashes |
| `assembly/assets/` | Black symbol derived from unchanged official vector artwork |
| `assembly/readme/` | In-use, printed-only, exploded and section illustrations |

Book order: cover; technical details; steps 1-4; steps 5-8; steps 9-12; full-page step 13; separate printed/hardware inventories; back cover. Four pictorial panels per instruction page. A4 landscape, 6 mm margins, 4 mm gutters, black 3 pt borders, no arrows, no panel prose. Quantities appear only above one. Only hardware has alpha links.

The HTML viewer starts at the landscape A4 page containing steps 1-4. It embeds the exact PDF page PNGs and their hardware hyperlink rectangles. Previous/next, keyboard arrows, Home/End and page selection navigate whole sheets. Zoom/pan preserves the 2 x 2 layout on phones. Browser printing uses A4 landscape pages with navigation hidden. Individual panels remain available through the written instructions. Publishing is separate; the landing README says hosting pending until a real served HTML endpoint is available.

## Sources and exceptions

- Printable geometry comes from the existing seven catalogue STLs. Their exact hashes are in the generated manifest. The reviewed axial stack is retained in `source_file/reviewed_inventory.json`.
- `components/kallax/cad.py` retains the production-mesh transforms and illustrative hardware from the earlier KALLAX renderer. `render_studio.py` uses catalogue STL paths, grouped physical instances and cumulative staging. Hardware threads are visual approximations.
- The booklet and viewer were adapted from the wave-drive implementation. See `components/kallax/PROVENANCE.md` for file hashes and local adaptations.
- Context illustrations in `source_file/context/` are the previously reviewed KALLAX source-CAD renders. The assembly views are newly rendered. Update context illustrations if the geometry changes; do not retain stale in-use images.
- Existing OOMP IDs/codes are retained for nuts, couplings and bolts. Their identity evidence was checked on 7 November 2026; redirect availability is not asserted. M6 x 300 rod remains **OOMP record pending**, explicitly accepted by the user. It receives no invented shortlink, even though the base standard permits project-local codes.
- No separate external design inspiration was established. Do not fabricate a creator credit. IKEA KALLAX names the compatible shelving system.
- The previous root `presentation/` and `renders/` are retained as historical source packages. They are not active deliverables. Existing catalogue STLs and source CAD are unchanged.

## Review

The build audits every physical instance, hardware identity code, source hash, cumulative stage and quantity. The booklet compositor rejects text overflow and verifies landscape pages, black typography, four-step sheets and signature padding. The viewer embeds all images. Validate local Markdown links and inspect every PDF page, the complete-pair image and both end-fastener operations. Keep digital checks separate from physical fit/load claims.

Use `pdftoppm` for an independent PDF raster review. The build also emits page PNGs through PyMuPDF. Browser review must include first/last navigation, keyboard controls and a narrow viewport. Do not edit generated PDF, PNG or HTML to fix defects; update the source and rebuild.

Initial review on 19 November 2026 (the one-step viewer is now superseded): eight pages inspected; 52 physical items and 70 local Markdown links reconciled. Desktop and 390 x 844 viewer layouts, next button, arrow key, step selector and Home/End endpoints were checked. The in-app browser rejects fullscreen and displays the intended fallback. Pointer drag did not verify touch swiping; check that on a touch device. Hosting remains pending. Regeneration updates the generated validation report; repeat visual review when its output hashes differ from `review.json`.

Four-step page viewer revision, 19 November 2026: the PDF and HTML now share the exact landscape page images. Default page 3 shows steps 1-4; following pages show 5-8 and 9-12. The validator checks byte-identical embedded page PNGs and expected step groups. Browser review confirmed page navigation, Home/End endpoints, legacy step links, page selection, and zoom/fit at 390 x 844. The reusable template is copied to OOBB base at `presentation/templates/assembly_page_viewer.html`.
