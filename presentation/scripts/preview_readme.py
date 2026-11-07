"""Render a local Markdown preview at desktop and narrow widths for visual QA.
Uses a local file and headless Edge; no publishing or network requests.
Optional dependencies: markdown, playwright (Python), installed Microsoft Edge.
"""
from pathlib import Path
import markdown
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'presentation'
html=markdown.markdown((ROOT/'readme.md').read_text(encoding='utf-8'),extensions=['tables','fenced_code'])
css='''body{margin:0;color:#24292f;background:white;font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}main{max-width:940px;margin:auto;padding:32px}h1{font-size:32px}h1,h2{line-height:1.3;border-bottom:1px solid #d8dee4;padding-bottom:.3em}h2{margin-top:32px}h3{margin-top:24px}a{color:#0969da;text-decoration:none}img{max-width:100%;height:auto}table{border-collapse:collapse;display:block;overflow-x:auto;max-width:100%}th,td{padding:6px 13px;border:1px solid #d0d7de}tr:nth-child(even){background:#f6f8fa}code{font:85% ui-monospace,Consolas,monospace;background:#eff1f3;padding:2px 4px;overflow-wrap:anywhere}li{margin:8px 0}p{margin:16px 0}@media(max-width:600px){main{padding:16px}h1{font-size:28px}}'''
target=P/'qa/readme-preview.html'
target.write_text(f'<!doctype html><html><head><meta charset="utf-8"><base href="{ROOT.as_uri()}/"><meta name="viewport" content="width=device-width,initial-scale=1"><style>{css}</style></head><body><main>{html}</main></body></html>',encoding='utf-8')
with sync_playwright() as pw:
    browser=pw.chromium.launch(channel='msedge',headless=True)
    for name,width,height in [('desktop',1200,1000),('narrow',390,844)]:
        page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
        page.route('http://**/*',lambda route:route.abort())
        page.route('https://**/*',lambda route:route.abort())
        page.goto(target.as_uri());page.wait_for_load_state('load')
        page.screenshot(path=str(P/'qa'/f'readme-{name}.png'))
        page.get_by_role('heading',name='Parts',exact=True).scroll_into_view_if_needed()
        page.screenshot(path=str(P/'qa'/f'readme-{name}-parts.png'))
        page.close()
    browser.close()
print('Rendered local README at 1200 px and 390 px widths')
