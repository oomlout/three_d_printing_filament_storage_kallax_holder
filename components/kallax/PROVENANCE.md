# Source provenance

Adapted on 19 November 2026 from the wave-drive style-4 implementation.

| Upstream file | SHA-256 |
| --- | --- |
| `components/wave_drive/assembly_booklet.py` | `ee7ebd035d27f3446ee54b64102a3b6b0410255765eecbf3ad201fd429815b57` |
| `components/wave_drive/assembly_viewer.py` | `47c59a251feeec154f0d5a5f3862010b628415b6e3286a861da00c5ea2452ca6` |
| `components/wave_drive/assembly_viewer.html` | `c1d2271261cb49e8472751577321b74e4e657d6145bc49bd93990a8f0d379eac` |

Local changes: import namespace changed to `components.kallax`; completed-view description names the holders. The local assembly adapter supplies the repository root and panel geometry. Mechanical recipes and source meshes are KALLAX-specific.

The unchanged official logo source is retained at `source_file/oomlout_logo_unshaded_original.svg`. Its SHA-256 and all active generator hashes are included in each generated assembly manifest.

The legacy geometry renderer was extracted from `render_kallax.py`. Its OpenSCAD STL transforms and hardware drawing functions are retained. New staging groups meshes by physical instance, audits cumulative inventory, and uses catalogue mesh paths. Context illustrations are retained from the reviewed prior package.

Viewer revision: whole landscape A4 pages replace the original wave-drive single-step web slideshow. The PDF remains four steps per instruction page. Page images and hyperlink rectangles are exported from that PDF; the base template is `presentation/templates/assembly_page_viewer.html`.
