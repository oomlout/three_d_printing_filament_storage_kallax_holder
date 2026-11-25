# Project location

The working project root is `C:\gh\three_d_printing_filament_storage_kallax_holder`.
The project moved from OneDrive on 7 November 2026. Use this checkout for all
project work and outputs.

Resolve project files relative to the script or repository root. Avoid embedding
the local checkout path in launchers, manifests, previews or new scripts. Existing
OOMP part IDs and GitHub URLs stay the same when the checkout moves.

The current documentation recipe is `working_oomp_populate.py`. Follow
`C:/gh/oomlout_oobb_version_5/ASSEMBLY_INSTRUCTIONS_GUIDE.md` (style 4),
`README_GUIDELINES.md` and `RENDER_STYLE.md`. The wave-drive assembly book is
the visual reference. This project's explicit all-black print colour overrides
the normal teal palette.

Run `python action_make_all.py` to populate the kit and its seven dependencies,
materialize their catalogue records, export CAD, render documentation and slice
the P1S project. `python working.py` rebuilds documentation from existing
catalogue meshes. Add `--no-renders` to reuse hash-validated diagrams.
See `DOCUMENTATION.md` for dependencies and commands.

Keep active documentation inside the one-cell version's `parts/` directory.
Use a compact version-index landing README, a full version README, ASSEMBLY.md,
an A4 landscape booklet, a standalone offline HTML viewer, manifest, CSV,
page PNGs, panel PNGs, thumbnails, contact sheet and validation report.
The PDF and default HTML viewer both show four steps in a 2 x 2 grid on each
landscape A4 instruction page. Open the viewer at steps 1-4; navigate by page.
Preserve landscape pages on phones and provide zoom rather than single-step reflow.
Do not edit generated documents. Author labels, steps, styles and book text
in populate. Reusable helpers live in `components/kallax/`.

Each cell has four short frames, four tall frames and four 300 mm M6 rods.
The holders are independent. Preserve recessed fixed nuts and bolt heads,
three spacer nuts and one coupling per rail, inner retaining nuts, 11 mm hex covers and 11 mm slotted
covers. The rod OOMP record remains pending by user instruction; do not invent
a catalogue record or shortlink. Printed parts have no alpha codes.

Use cumulative source-CAD views, black typography, no arrows or prose on
instruction panels, and the official black Oomlout symbol. Every physical
instance must appear exactly once in the added inventory. Include both holders
in the written and pictorial sequence. Keep prior installed pieces in view.

The original `presentation/` package and `render_kallax.py` are historical
layout-4 sources, retained for traceability. They are not the active build.
Do not let old scripts replace the new landing README or booklet. New outputs
belong in the version directory, not in another root presentation folder.

Hosting is separate from generation. Only set a hosted viewer URL after it
has been published and checked. Do not describe a GitHub HTML blob as a viewer.

Shared OOMP data, OOBB libraries, system fonts, installed applications and the
cross-project lock under `C:\gh\oomlout_base\lock` are external dependencies;
their paths are independent of this project's root.

The combined one_cell_kit folder owns all active assembly instructions, printable STL copies and the P1S project. The coupling housing is 18 mm. The two 11 mm covers overlap by 8 mm. Edit the Python definitions and rebuild. Treat the catalogue records, SCAD files, meshes and print plates as generated outputs.
