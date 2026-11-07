"""Apply revision 3: concise technical instructions and verified lookup codes."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
path=ROOT/'presentation/project.json'
d=json.loads(path.read_text(encoding='utf-8'));d['revision']='3'
codes={'H2':'hcps','H3':'1qsz8','H4':'9dg7e'}
for p in d['hardware']:
    if p['ref']=='H1':
        p['url']='https://www.ecfibreglasssupplies.co.uk/grade-48-zinc-threaded-rod-m6-x-300-mm'
        p['verification']='Supplier product verified 2026-11-06: M6 x 300 mm fully threaded zinc-plated steel; no verified OOMP ID'
    if p['ref'] in codes:
        p['md5_6_alpha']=codes[p['ref']]
        p['code_verified']='Public OOMP record inspected 2026-11-06'
for p in d['printed_parts']:
    p['md5_6_alpha']=None
    p['code_verified']='No md5_6_alpha field in the local catalogue record; direct STL link retained'
r=d['readme']
source=ROOT/'presentation/source-notes.json'
if not source.exists():source.write_text(json.dumps(r,indent=2),encoding='utf-8')
r.update({
 'summary':'Two independent holders per KALLAX cell: five front reels and five raised rear refills. Four side frames and two M6 rails per holder.',
 'validation_status':'',
 'configuration':'Front: 4 short frames. Rear: 4 tall frames. Rail heights: 37 / 112 mm. Row centres: 187 mm. Nominal cell width: 335 mm.\n\nIllustrated rolls: front diameter 200 x 60 mm wide; rear diameter 200 x 58 mm wide. Five rolls at 62 mm centres occupy 308 mm.',
 'quantity_basis':'one complete cell',
 'quantity_note':'Double for two cells. Print all 32 plastic parts in black.',
 'hardware_notes':'Click an MD5 alpha code for its OOMP record. H2 includes fixed and retaining nuts. H4 is a fully threaded hex-head set screw.',
 'preparation':'Measure the opening. Check the 5 mm hex pockets against the nuts and bolt heads. Cut and deburr four 300 mm M6 rods. Prepare a 10 mm spanner.',
 'assembly_steps':[
 'Seat two H2 nuts in the first frame\'s outer hex pockets. Thread in H1 rods; keep the ends flush.',
 'Fit both rails in this order: P3 sleeve / second frame / P4 sleeve / third frame / P3 sleeve. Face the last sleeve\'s hex pocket toward the coupling.',
 'Insert H3 couplings into P5 housings. Thread onto the rods to approximately 6 mm engagement.',
 'Face the final frame\'s hex pockets outward. Insert H4 bolts. Add H2 retaining nuts loosely. Slide P6 hex covers onto the bolts.',
 'Thread H4 into H3. Set the span. Seat the bolt heads. Slide P6 aside, tighten H2 against the inner frame face, then cover the nuts.',
 'Clip P7 over each exposed thread section. Check all end fasteners are recessed. Repeat with tall frames.'
 ],
 'adjustment':'Per rail: one 18 mm coupling, one M6 x 25 bolt, one retaining M6 nut, one 7 mm hex cover and one 7 mm slotted cover.\n\nTo adjust: remove P7; slide P6 aside; loosen H2; release the bolt head from its recess; turn H4. Reseat the head, tighten H2 and refit both covers.',
 'installation_steps':[
 'Place the tall holder at the rear and the short holder at the front. Seat all feet on the shelf.',
 'Check width and fastener seating before loading. Do not force the cabinet sides apart.',
 'Load strapped rear refills, then front reels. Check clearance and frame stability.'
 ],
 'dimensions':'Nominal rail stack: `4 x 9 + 2 x 99.67 + 67.67 + 18 + 7 + 7 = 335.01 mm`.\n\nM6 x 25 bolt: 7 mm nominal coupling engagement; 5.01 mm tip clearance. Rod engagement: 5.99 mm. Slotted cover length for another opening: `opening - 328.01 mm`; recheck engagement before use.',
 'verification':'',
 'sources':'[STL files](scad_output) · [Catalogue parts](parts) · [Coupling dimensions](https://www.accu.co.uk/hexagonal-stud-connector-nuts/62290-HTBN-M6-A2) · [KALLAX reference](https://www.ikea.com/gb/en/p/kallax-shelving-unit-white-30275861/) · [Research notes](presentation/research.md)'
})
path.write_text(json.dumps(d,indent=2),encoding='utf-8')
print('Revision 3: concise instructions; combined BOM; verified MD5 alpha codes')
