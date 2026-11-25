# One-cell kit build

Run from the repository root on Windows.

```powershell
python -m pip install -r components/kallax/requirements.txt
python action_make_all.py
```

Install OpenSCAD and Blender on PATH. The slice check uses Bambu Studio from PATH or its standard Windows installation. The full build reads the Python sources, the viewer template, the reviewed dimensions, the logo and the default 3MF under `source_file/`. It can start with empty `parts_source/` and `parts/` directories.

| Stage | Source | Output |
| --- | --- | --- |
| Populate | `working_oomp_populate.get_options()` | Eight `parts_source/<id>/working.yaml` records. The kit defines component IDs, quantities, hardware and assembly steps. |
| Catalogue | `working_oomp.catalogue()` | Corresponding `parts/<id>/working.yaml` records. |
| CAD | `working_scad.main()` and `components/kallax/kit_geometry.py` | Seven individual SCAD and STL pairs. The kit’s standalone `3dpr.scad` embeds the same seven definitions and positions all 32 printed pieces using `instances.py`. |
| Package | `components/kallax/build.py` | Assembly images, booklet, offline viewer, READMEs, print STLs and the three-plate P1S project. |
| Slice | `components/kallax/print_project.py` | Bambu Studio slices all three plates. The kit retains the result in `print/slice_validation.json`. |

Edit dimensions, quantities and steps in `working_oomp_populate.py`, profiles in `kit_geometry.py`, installed positions in `instances.py` and print placement in `print_project.py`. The frame profile retains the released 5 mm corner radius. Open the [one-cell kit](parts/project_github_oomlout_three_d_printing_filament_storage_kallax_one_cell_kit/README.md) for the print project and instructions.

For documentation edits, `python working.py` renders the current catalogue meshes. Use `python working.py --no-renders` to recompose the pages from verified cached diagrams.

Each rail uses five ordinary M6 nuts. The nuts after the first and centre spacers seat in frames 2 and 3. The third spacer nut seats flush in the final 99.67 mm spacer at the coupling. All three fit within existing 5 mm recesses.

For one rail the fixed hardware and four 9 mm frames retain the nominal 335.01 mm span. The 18 mm coupling housing ends at 312.01 mm. The 11 mm slotted cover runs from 312.01 to 323.01 mm. The 11 mm hex retaining cover runs from 315.01 to 326.01 mm. Their 8 mm overlap leaves a 3 mm neck over the exposed bolt thread. The clip socket is 14.6 mm across over a 14 mm cover, with a 13.8 mm opening. Snap fit is untested. Rod engagement is 5.99 mm and bolt engagement is 7 mm.

The printable booklet and standalone viewer use the same four-step landscape A4 sheets. Assembly instructions are published only inside the kit. The earlier one-cell folder redirects readers to it. Historical development files under presentation and renders predate this design.

The starter project in `source_file/default.3mf` is an unchanged copy of `three_d_printing_base/default.3mf`. The P1S builder retains its project settings byte for byte. The project uses the P1S 0.4 mm nozzle, textured PEI, oobb_base_layer_p1s process and black Bambu PLA Basic in slot 1. Build plate previews are drawn from the actual print meshes. The kit contains editable plate geometry. Open in Bambu Studio, select the plate and slice.

Digital validation covers each physical instance, plate count and footprint, generated links, signature-padded PDF and HTML page images. The project is AI-generated. Physical fit and load capacity remain untested.

The P1S packager vendors the OOBB base editable-copy writer in `components/kallax/p1s_print_kit.py`. Each physical piece has its own object and normal part. The archive is checked against the 32-piece BOM before replacement.
