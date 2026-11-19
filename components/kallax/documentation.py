"""Generate the landing page and complete written version instructions."""
from PIL import Image
from .assembly_cards import ROOT

def publish(**kwargs):
    folder,output,data=(kwargs[k] for k in ['folder','output','data'])
    def write(path,text):path.write_text(text,encoding='utf-8')
    thumbs=output/'thumbnails';thumbs.mkdir(exist_ok=True)
    for step in data['steps']:
        with Image.open(output/'cards'/(step['key']+'.png')) as image:
            image.thumbnail((480,480));image.save(thumbs/(step['key']+'.png'))
    printed=['| Part | Size | Qty. | Print file |','| --- | --- | ---: | --- |']
    hardware=['| Part | Specification | Qty. | OOMP ID | Code |','| --- | --- | ---: | --- | --- |']
    for key,p in data['parts'].items():
        if key in data['printed_keys']:
            printed.append(f"| {p['name']} | {p['detail']} | {p['quantity']} | [STL](../../{p['stl']}) |")
        else:
            link=f"[{p['name']}]({p['url']})" if p.get('url') else p['name']
            identity=f"[{p['id']}]({p['url']})" if p.get('url') else 'OOMP record pending'
            code=f"[{p['md5_6_alpha']}]({p['short_url']})" if p.get('short_url') else '-'
            hardware.append(f"| {link} | {p['detail']} | {p['quantity']} | {identity} | {code} |")
    notice='AI-generated CAD images and instructions. Errors possible.'
    steps=[]
    for s in data['steps']:
        steps.append(f"{s['number']}. {s['action']}\n\n   [![AI-generated assembly step {s['number']}](assembly/thumbnails/{s['key']}.png)](assembly/cards/{s['key']}.png)")
    installation=data['readme']['installation']
    detail=f"# KALLAX filament holders - one cell\n\n{notice}\n\n[PDF booklet](assembly/assembly_instructions.pdf) · [Standalone HTML viewer](assembly/assembly_instructions.html) · [Full BOM](assembly/parts.csv)\n\n## Summary\n\n{data['readme']['summary']}\n\n![AI-generated CAD: one loaded KALLAX cell](assembly/readme/cell.png)\n\n## Details\n\nTwo independent holders. Four short frames at the front; four tall frames at the rear. Nominal width: 335 mm. Rail heights: 37 / 112 mm. Row centres: 187 mm. Print all plastic parts in black. Physical fit and load capacity are untested.\n\n![AI-generated CAD: assembled printed parts](assembly/readme/printed.png)\n\nTwo cells in a 4 x 4 KALLAX unit; double the quantities below.\n\n![AI-generated CAD: two populated KALLAX cells](assembly/readme/cabinet.png)\n\n## Parts\n\nOne complete cell. Short holder shown exploded; the rear uses tall frames.\n\n![AI-generated exploded short holder](assembly/readme/exploded.png)\n\n### Printed parts\n\n"+'\n'.join(printed)+'\n\n### Hardware\n\n'+'\n'.join(hardware)+"\n\nBolt length is measured under the head. Threaded rod: OOMP record pending.\n\n## Assembly\n\nCut and deburr four 300 mm M6 rods. Prepare a 10 mm spanner. Steps 1-6 build the short holder; steps 7-12 build the tall holder.\n\n"+'\n\n'.join(steps)+f"\n\n### Installation\n\n{installation}\n\n![AI-generated section of the adjustable end](assembly/readme/end-section.png)\n\nPer rail: one coupling; one fixed nut; one retaining nut; one 25 mm bolt. Nominal engagement: rod 5.99 mm, bolt 7 mm. A different span requires a revised slotted cover and an engagement check.\n"
    write(folder/'README.md',detail)
    write(folder/'ASSEMBLY.md',f'# Assembly\n\n{notice}\n\n[PDF booklet](assembly/assembly_instructions.pdf) · [Standalone viewer](assembly/assembly_instructions.html)\n\n'+'\n\n'.join(steps)+f'\n\n## Installation\n\n{installation}\n')
    rel=folder.relative_to(ROOT).as_posix()
    hosted=data['readme'].get('viewer_url')
    viewer=f'[Open in browser]({hosted})' if hosted else f'Hosting pending · [Download HTML]({rel}/assembly/assembly_instructions.html)'
    hero_link=hosted or f'{rel}/README.md'
    landing=f"# {data['readme']['title']}\n\n{data['readme']['summary']}\n\n{data['readme']['ai_notice']} Physical fit and load capacity have not been tested.\n\n> {notice}\n\n## Versions\n\n| Image | Version and description | Main README | HTML assembly instructions | PDF download |\n| --- | --- | --- | --- | --- |\n| [![AI-generated CAD: KALLAX filament holders]({rel}/assembly/readme/thumbnail.png)]({hero_link}) | **{data['readme']['version_title']}**<br>{data['readme']['version_description']} | [README]({rel}/README.md) | {viewer} | [Download PDF]({rel}/assembly/assembly_instructions.pdf) |\n"
    write(ROOT/'readme.md',landing)
