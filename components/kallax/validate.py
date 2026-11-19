"""Check the generated Markdown, standalone viewer and cumulative inventory."""
from collections import Counter
from pathlib import Path
import json, re
from urllib.parse import unquote
from PIL import Image
from .assembly_cards import ROOT

def main(**kwargs):
    output=Path(kwargs['output']); folder=output.parent
    data=json.loads((output/'assembly_manifest.json').read_text())
    refs=0
    for file in [ROOT/'readme.md',folder/'README.md',folder/'ASSEMBLY.md']:
        for target in re.findall(r'\]\(([^)]+)\)',file.read_text(encoding='utf-8')):
            if target.startswith(('https://','http://','#')):continue
            path=(file.parent/unquote(target.split('#')[0])).resolve()
            if not path.exists():raise ValueError(f'Missing link in {file.name}: {target}')
            refs+=1
    records={r['name']:r for r in data['instances']}
    seen=set();counts=Counter()
    for step in data['steps']:
        assert not seen.intersection(step['added_instances'])
        seen.update(step['added_instances'])
        assert set(step['shown_instances'])==seen
        counts.update(step['loose_parts'])
        with Image.open(output/'thumbnails'/(step['key']+'.png')) as im:assert max(im.size)<=480
    assert seen==set(records)
    assert counts==Counter({k:p['quantity'] for k,p in data['parts'].items()})
    html=(output/'assembly_instructions.html').read_text(encoding='utf-8')
    payload=json.loads(re.search(r'<script id="viewer-data" type="application/json">(.*?)</script>',html,re.S).group(1))
    assert payload['start']=='page-03'
    assert payload['layout']=='a4-landscape-four-step'
    assert payload['paper_mm']==[297,210]
    assert len(payload['slides'])==len(data['book_pages'])==8
    instruction_pages=[s for s in payload['slides'] if s['kind']=='instructions']
    assert [s['steps'] for s in instruction_pages]==[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    import base64
    for slide in payload['slides']:
        embedded=base64.b64decode(payload['images'][slide['image']].split(',',1)[1])
        assert embedded==(output/'pages'/f"page_{slide['number']:02d}.png").read_bytes()
    assert all(value.startswith('data:image/png;base64,') for value in payload['images'].values())
    assert not re.search(r'<(?:script|link|img)\b[^>]*(?:src|href)=["\']https?://',html)
    allowed={p['short_url'] for p in data['parts'].values() if 'short_url' in p}
    allowed.add(data['book']['project_url'])
    assert all(link['url'] in allowed for slide in payload['slides'] for link in slide['links'])
    report_path=output/'validation.json'
    report=json.loads(report_path.read_text())
    report.update(local_markdown_links=refs,thumbnail_count=len(data['steps']),viewer_embedded_assets=len(payload['images']),viewer_external_asset_count=0,cumulative_inventory_verified=True,viewer_pages_match_pdf=True)
    report_path.write_text(json.dumps(report,indent=2))
    return report
