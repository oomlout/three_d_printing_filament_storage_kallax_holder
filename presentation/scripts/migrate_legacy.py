"""One-time reversible migration of old presentation entry points.
Backups are retained in presentation/qa/legacy. Normal builds do not run this.
"""
from pathlib import Path
import shutil
ROOT=Path(__file__).resolve().parents[2]
backup=ROOT/'presentation/qa/legacy';backup.mkdir(parents=True,exist_ok=True)
for relative in ('make_visual_guide.py','renders/README.md','readme.md'):
    src=ROOT/relative;dest=backup/relative.replace('/','_')
    if src.exists() and not dest.exists():shutil.copy2(src,dest)
(ROOT/'make_visual_guide.py').write_text('"""Compatibility entry point for the current presentation builder."""\nfrom pathlib import Path\nimport runpy\nrunpy.run_path(str(Path(__file__).resolve().parent / "presentation/scripts/build.py"), run_name="__main__")\n',encoding='utf-8')
(ROOT/'renders/README.md').write_text('# Historical presentation outputs\n\nThese renders belong to the previous assembly revision. Use the current [presentation package](../presentation/README.md), [assembly guide](../presentation/assembly-guide.pdf) and [project README](../readme.md).\n\nRevision 2 includes the bolt-retaining nut, a 7 mm full-hex nut cover and a 7 mm slotted cover. The prior 14 mm clip is superseded for this assembly.\n',encoding='utf-8')
readme=ROOT/'readme.md';text=readme.read_text(encoding='utf-8')
marker='<!-- oobb-presentation:end -->'
if marker in text:
    head,tail=text.split(marker,1)
    # Remove only the inspected old boilerplate; the old file is in the backup.
    if tail.lstrip().startswith('# Three D Printing Filament Storage Kallax Holder'):
        readme.write_text(head+marker+'\n',encoding='utf-8')
print('Migrated legacy entry points; original files retained in presentation/qa/legacy')
