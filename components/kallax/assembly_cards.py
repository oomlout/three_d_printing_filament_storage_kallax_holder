"""Local adapter for the wave-drive style 4 booklet compositor."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]

def panel_geometry(style):
    width, height = style['page_mm']
    return ((width-2*style['margin_mm']-(style['columns']-1)*style['gutter_mm'])/style['columns'],
            (height-2*style['margin_mm']-(style['rows']-1)*style['gutter_mm'])/style['rows'])
