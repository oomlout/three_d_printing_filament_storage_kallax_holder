"""Typeset the KALLAX visual / assembly guide from the CAD renders."""
from pathlib import Path
import math,json,csv,shutil
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor,Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'renders'; PDF=ROOT/'output/pdf';PDF.mkdir(parents=True,exist_ok=True)
W,H=900,675
for name,filename in [('Regular','segoeui.ttf'),('Bold','segoeuib.ttf'),('Mono','consola.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(Path('C:/Windows/Fonts')/filename)))
INK='#20292B';MUTED='#626C6D';TEAL='#007E83';PALE='#E4EEEB';PAPER='#F6F3EC';YELLOW='#FEC601'
c=canvas.Canvas(str(PDF/'kallax_filament_visual_assembly_guide.pdf'),pagesize=(W,H))
c.setTitle('Filament, neatly shelved | KALLAX holder visual and assembly guide')
c.setAuthor('OOBB / oomlout')
def rect(x,y,w,h,col):
    c.setFillColor(HexColor(col));c.rect(x,H-y-h,w,h,fill=1,stroke=0)
def text(x,y,s,size=11,font='Regular',color=INK):
    c.setFont(font,size);c.setFillColor(HexColor(color));c.drawString(x,H-y-size*.8,s)
def lines(x,y,rows,size=11,leading=17,font='Regular',color=INK):
    for i,s in enumerate(rows):text(x,y+i*leading,s,size,font,color)
def line(x1,y1,x2,y2,color='#BAC8C4',width=.65):
    c.setStrokeColor(HexColor(color));c.setLineWidth(width);c.line(x1,H-y1,x2,H-y2)
def image(name,x,y,w,h):
    p=OUT/'raw'/f'{name}.png';im=ImageReader(str(p));iw,ih=im.getSize()
    sc=min(w/iw,h/ih);dw,dh=iw*sc,ih*sc
    c.drawImage(im,x+(w-dw)/2,H-y-(h+dh)/2,dw,dh)
    return lambda a,b:(x+(w-dw)/2+a*dw,y+(h-dh)/2+b*dh)
def callout(project,shot,key,x,y,label):
    anchors=json.loads((OUT/'raw'/f'{shot}_anchors.json').read_text())
    px,py=project(*anchors[key])
    line(px,py,x+15 if y>py else x,y-4 if y>py else y+12,TEAL,.65)
    c.setFillColor(HexColor(TEAL));c.circle(px,H-py,2,fill=1,stroke=0)
    text(x,y,label,10,'Bold',TEAL)
def badge(project,shot,key,dx,dy):
    anchors=json.loads((OUT/'raw'/f'{shot}_anchors.json').read_text())
    px,py=project(*anchors[key]);x,y=px+dx,py+dy
    line(px,py,x+10,y+10,TEAL)
    rect(x,y,20,20,TEAL);text(x+6,y+4,key,12,'Bold','#FFFFFF')
def page(num,title,sub):
    rect(0,0,W,H,PAPER)
    text(35,24,'OOBB   /   FILAMENT STORAGE',9,'Mono',TEAL)
    text(35,49,title,31,'Bold')
    text(36,91,sub,11,color=MUTED)
    line(35,120,865,120)
    line(35,638,865,638)
    text(35,651,'KALLAX HOLDERS   /   CAD-BASED ASSEMBLY STUDY   /   05 NOV 2026',8,'Mono',MUTED)
    text(817,650,f'{num:02d} / 07',8,'Mono',MUTED)
def finish():c.showPage()
def tag(x,y,n,title,body):
    rect(x,y,25,24,TEAL);text(x+7,y+5,str(n),12,'Bold','#FFFFFF')
    text(x+37,y,title,14,'Bold');lines(x+37,y+24,body,10,15,color=MUTED)
def dim(x1,y1,x2,y2,label,above=True):
    line(x1,y1,x2,y2,TEAL,.8)
    if abs(y2-y1)<1:
        for x in (x1,x2):line(x,y1-4,x,y1+4,TEAL)
        tw=pdfmetrics.stringWidth(label,'Mono',9)
        text((x1+x2-tw)/2,y1-18 if above else y1+7,label,9,'Mono',TEAL)
    else:
        for y in (y1,y2):line(x1-4,y,x1+4,y,TEAL)
        text(x1+8,(y1+y2)/2-6,label,9,'Mono',TEAL)
def palette(y):
    for x,col,s in [(40,'121212','Black printed parts'),(213,'00B1B7','Teal filament'),(354,'FEC601','Sunflower filament')]:
        rect(x,y,11,11,'#'+col);text(x+18,y,s,9,color=MUTED)

page(1,'Filament, neatly shelved.','Five full reels in front. Spool-free refills behind. Two independent black holders.')
image('cell',17,130,570,470)
text(606,163,'ONE CELL',10,'Mono',TEAL)
text(605,188,'A place for every roll.',21,'Bold')
lines(606,228,['Four short frames support the front reels.','Four tall frames support the rear refills.','The two holders stand independently.'],11,19)
line(606,300,853,300)
for y,big,small in [(320,'5 + 5','Full reels + illustrated refills'),(402,'4 x 300 mm','M6 threaded rods per complete cell'),(484,'All black','Satin printed frames, sleeves and grips')]:
    text(606,y,big,25,'Bold');text(606,y+36,small,10,color=MUTED)
palette(605)
finish()

page(2,'Two cells. One tidy wall.','The same front-and-back setup, repeated in a white 4 x 4 KALLAX.')
image('cabinet',10,130,640,490)
text(667,164,'4 x 4 KALLAX',10,'Mono',TEAL)
text(666,190,'Room to grow.',22,'Bold')
lines(667,232,['Two populated cells are shown.','Each contains five front reels and','five raised rear refills.'],11,18)
rect(666,319,195,102,PALE)
text(681,335,'FOR TWO CELLS',9,'Mono',TEAL)
text(681,359,'8 rods / 4 holders',17,'Bold')
text(681,389,'Double the one-cell parts list.',10,color=MUTED)
lines(667,464,['Shelf envelope:','1470 W x 1470 H x 390 D mm','Nominal cell used in this model:','335 W x 335 H x 390 D mm'],10,19,color=MUTED)
lines(667,562,['Furniture dimensions: IKEA UK.','Internal cell is a modelling assumption;','measure the actual unit before fitting.'],8.5,13,color=MUTED)
c.linkURL('https://www.ikea.com/gb/en/p/kallax-shelving-unit-white-30275861/',(667,H-604,862,H-464),relative=0,thickness=0)
finish()

page(3,'Four frames in each holder.','Four short frames at the front. Four tall frames at the rear. The two holders do not connect.')
project=image('empty',25,138,530,365)
badge(project,'empty','A',-35,10);badge(project,'empty','B',20,-15);badge(project,'empty','C',-60,-30)
text(586,154,'THE GEOMETRY',10,'Mono',TEAL)
tag(586,188,'A','Short front holder',['4 side frames, nominally 149 x 44 x 9 mm.','Top rail centres are 37 mm above the shelf.'])
tag(586,280,'B','Tall rear holder',['4 side frames, nominally 149 x 119 x 9 mm.','Top rail centres are 112 mm above the shelf.'])
tag(586,372,'C','Two rails through all four frames',['Each rail uses one 300 mm M6 rod.','One coupling nut and one bolt adjust its span.'])
rect(35,510,830,108,PALE)
text(52,525,'PLACE THEM FRONT TO BACK',10,'Mono',TEAL)
lines(52,550,['The illustration uses 187 mm between row centres, giving about 38 mm between the frame bodies.',
              'Both holders rest directly on the shelf. Their rail heights differ by 75 mm.',
              'Place and check the rear refills first, then add the front reels. Keep refill retaining straps fitted.'],11,19)
finish()

page(4,'Build one rail. Repeat four times.','One 300 mm M6 threaded rod per rail. Two rails per holder. Four rails per complete cell.')
project=image('rail',35,127,830,300)
callout(project,'rail','rod',230,145,'M6 x 300 mm')
callout(project,'rail','long',185,380,'99.67 mm')
callout(project,'rail','centre',355,380,'67.67 mm')
callout(project,'rail','nut',620,380,'One coupling nut')
callout(project,'rail','grip',540,170,'18 mm nut housing')
callout(project,'rail','clip',707,170,'14 mm slotted cover')
callout(project,'rail','bolt',750,380,'M6 x 25 bolt')
callout(project,'rail','fixed',62,180,'Captive M6 nut')
text(46,434,'SLEEVE ORDER, LEFT TO RIGHT',9,'Mono',TEAL)
text(46,455,'99.67 mm  +  67.67 mm  +  99.67 mm  =  267.01 mm',20,'Bold')
line(35,497,865,497)
tag(41,515,1,'Fit the fixed-end nut',['Seat one M6 nut inside the first frame.','Thread in the deburred 300 mm rod.'])
tag(327,515,2,'Alternate sleeves and frames',['Frame / 99.67 / frame / 67.67 / frame /','99.67 / nut housing / cover / final frame.'])
tag(610,515,3,'Recess both end fasteners',['One coupling nut sits inside its housing.','The bolt head seats inside the final frame.'])
text(46,609,'Lengths in mm. Standard M6 x 18 coupling; calculated M6 x 25 bolt and 14 mm cover for a nominal 335 mm opening.',9,color=MUTED)
finish()

page(5,'The parts list.','Quantities below make one complete cell: one short front holder plus one tall rear holder.')
rows=[
('Short side frame','149 x 44 x 9 mm','4','8'),
('Tall side frame','149 x 119 x 9 mm','4','8'),
('Long sleeve, one-end nut pocket','99.67 mm long / 14 mm diameter','8','16'),
('Centre sleeve, one-end nut pocket','67.67 mm long / 14 mm diameter','4','8'),
('Coupling nut housing, full hex bore','18 mm long / 14 mm diameter','4','8'),
('Slotted end cover (new variant)','14 mm long / original 9 mm profile','4','8'),
('M6 threaded rod','300 mm cut length','4','8'),
('M6 captive fixed-end nut','5 mm nominal thickness / 10 mm AF','4','8'),
('M6 coupling nut, DIN 6334','18 mm long / 10 mm across flats','4','8'),
('M6 hex-head bolt, fully threaded','25 mm under-head length','4','8')]
rect(35,140,830,33,TEAL)
for x,s in [(49,'PART'),(384,'DIMENSIONS'),(680,'1 CELL'),(775,'2 CELLS')]:text(x,151,s,10,'Mono','#FFFFFF')
for i,(name,dimens,one,two) in enumerate(rows):
    y=173+i*30
    rect(35,y,830,30,'#FFFFFF' if i%2==0 else '#EDEFE9')
    text(49,y+10,name,10.7,'Bold' if i<2 else 'Regular')
    text(384,y+10,dimens,10,color=MUTED)
    text(699,y+9,one,12,'Bold');text(798,y+9,two,12,'Bold')
text(43,489,'The 14 mm cover replaces the 9 mm cover for this nominal 335 mm opening. Measure your actual cell.',9,color=MUTED)
rect(35,519,405,95,PALE);rect(454,519,411,95,'#F0E8D1')
text(50,533,'PRINT IN BLACK',10,'Mono',TEAL)
lines(50,554,['28 printed pieces per complete cell.','Original parts are unchanged; a 14 mm clip is added.','See renders/parts_manifest.csv for exact STL paths.'],10,16)
text(469,533,'LENGTH CHECK',10,'Mono',TEAL)
lines(469,554,['267.01 + 4 x 9 + 18 + 14 = 335.01 mm overall.','The 0.01 mm difference is rounding of CAD lengths.','Both end fasteners sit within their frame recesses.'],10,16)
finish()

page(6,'Assemble, position, load.','Use the same assembly sequence for the short and tall holders.')
image('exploded',18,133,510,318)
tag(544,150,1,'Seat the captive fixed-end nut',['Fit the M6 nut in the first frame hex pocket.','Thread the rod into it; keep the fixed end flush.'])
tag(544,236,2,'Thread the sleeves and middle frames',['Alternate the three long sleeves and first 3 frames.','Add the coupling nut inside its 18 mm housing.'])
tag(544,322,3,'Seat the bolt, then clip on the cover',['Turn the final frame so its hex recess faces out.','Seat the M6 x 25 bolt head in it; thread into the coupling.','Clip the 14 mm slotted cover over the last exposed thread.'])
line(35,457,865,457)
text(41,478,'CHECK THE FIT',10,'Mono',TEAL)
lines(41,504,['The illustrated reels are generic narrow reels: 200 mm diameter x 60 mm wide.',
             'Five at 62 mm centres occupy 308 mm. This is a dimensional illustration, not a brand-fit guarantee.',
             'Rear refills are shown at 200 mm diameter x 58 mm wide, with their retaining straps fitted.',
             'Check your actual rolls, coupling nuts and shelf opening. This guide does not establish a load rating.'],10.5,18)
text(41,594,'SOURCE NOTES',8,'Mono',TEAL)
lines(41,610,['Production side/sleeve meshes: project scad_output. Finish and presentation: OOBB RENDER_STYLE.md.'],8,color=MUTED)
finish()

page(7,'Recessed ends. Covered thread.','One captive nut, one coupling and one M6 x 25 bolt per rail. The slotted end cover completes the span.')
# True axial section of the illustrated setting. Coordinates measured from the fixed end.
sx=7.5; x0=75; cy=270
def xx(v):return x0+(v-280)*sx
def section(a,b,outer,inner,col):
    rect(xx(a),cy-outer*sx,(b-a)*sx,(outer-inner)*sx,col)
    rect(xx(a),cy+inner*sx,(b-a)*sx,(outer-inner)*sx,col)
section(280,289.01,7,3.25,'#232829')
section(289.01,294.01,7,5.91425,'#232829')
section(294.01,312.01,7,5.91425,'#232829')
# Clip section through its downward-facing slot: upper wall only.
rect(xx(312.01),cy-7*sx,14*sx,(7-3.25)*sx,'#232829')
section(326.01,330.01,7,3.25,'#232829')
section(330.01,335.01,7,5.91425,'#232829')
section(294.01,312.01,5.77,3,'#8C9A9E')
rect(xx(280),cy-2.7*sx,(300-280)*sx,5.4*sx,'#B1BCBF')
rect(xx(305.01),cy-2.7*sx,25*sx,5.4*sx,'#B1BCBF')
rect(xx(330.01),cy-5.77*sx,4*sx,11.54*sx,'#8C9A9E')
for v in range(281,300):line(xx(v),cy-2.7*sx,xx(v)+3,cy+2.7*sx,'#7C8B8F',.55)
for v in range(306,330):line(xx(v),cy-2.7*sx,xx(v)+3,cy+2.7*sx,'#7C8B8F',.55)
for v in (294.01,312.01,326.01):
    line(xx(v),cy-7*sx,xx(v),cy-5.91425*sx,PAPER,1.4)
    line(xx(v),cy+5.91425*sx,xx(v),cy+7*sx,PAPER,1.4)
dim(xx(294.01),168,xx(312.01),168,'18 mm coupling')
line(xx(294.01),173,xx(294.01),219,TEAL);line(xx(312.01),173,xx(312.01),219,TEAL)
dim(xx(312.01),353,xx(326.01),353,'14 mm clip',False)
text(78,398,'SLEEVE',9,'Mono',TEAL)
text(215,398,'NUT HOUSING',9,'Mono',TEAL)
text(406,398,'END FRAME',9,'Mono',TEAL)
text(604,159,'BOTH ENDS ARE RECESSED',9,'Mono',TEAL)
lines(604,186,['Fixed nut: inside the first frame pocket.','Bolt head: inside the final frame pocket.','The final frame faces the opposite way.'],10,18)
text(604,265,'WHY AN M6 x 25 BOLT?',9,'Mono',TEAL)
lines(604,292,['The seated head bearing face is at 330.01 mm.','A 25 mm bolt ends at 305.01 mm, giving','7 mm engagement in the coupling and','5.01 mm clearance to the 300 mm rod end.','Rod engagement is 5.99 mm (nominally 6 mm).'],9.5,18)
rect(35,459,830,151,PALE)
text(52,475,'CALCULATED FOR A NOMINAL 335 mm CELL',10,'Mono',TEAL)
lines(52,502,['Cover length = opening - (267.01 mm sleeves + 36 mm frames + 18 mm nut housing).',
              'For 335 mm this is 13.99 mm, rounded to a 14 mm printed cover. The 9 mm cover leaves about 5 mm exposed.',
              'A 20 mm bolt gives only 2 mm engagement; a 30 mm bolt almost touches the rod. The 25 mm bolt leaves clearance.',
              'Measure the actual opening and check the assembled fit. Thread figures are geometric, not a tested load rating.'],10.2,20)
text(52,597,'Hardware reference: Accu M6 DIN 6334 connector nut (18 mm long, 10 mm AF).',8,color=MUTED)
c.linkURL('https://www.accu.co.uk/hexagonal-stud-connector-nuts/62290-HTBN-M6-A2',(52,H-610,650,H-591),relative=0,thickness=0)
finish();c.save()

prefix='project_github_oomlout_three_d_printing_filament_storage_kallax_'
manifest=[
('Short side frame',4,'side_10_width_3_height_9_mm_depth_short_extra'),
('Tall side frame',4,'side_10_width_8_height_9_mm_depth_short_extra'),
('99.67 mm sleeve',8,'spacer_1_width_1_height_99_67_mm_depth_one_end_nut_extra'),
('67.67 mm sleeve',4,'spacer_1_width_1_height_67_67_mm_depth_one_end_nut_extra'),
('18 mm coupling nut housing',4,'spacer_1_width_1_height_18_mm_depth_full_nut_extra'),
('14 mm slotted end cover',4,'spacer_1_width_1_height_14_mm_depth_slotted_extra')]
with (OUT/'parts_manifest.csv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.writer(f);writer.writerow(['part','quantity_per_cell','quantity_two_cells','source_stl'])
    for name,qty,part in manifest:
        path=ROOT/'parts'/(prefix+part)/'3dpr.stl'
        assert path.exists(),path
        writer.writerow([name,qty,qty*2,str(path)])
        # House rule: save presentation PNGs alongside the actual production STLs.
        shot='cell' if part.startswith('side') else 'rail'
        shutil.copy2(OUT/'raw'/f'{shot}.png',path.parent/'presentation_assembled.png')
        shutil.copy2(OUT/'raw'/('exploded.png' if part.startswith('side') else 'rail.png'),path.parent/'presentation_exploded.png')
    writer.writerow(['M6 threaded rod, 300 mm',4,8,'Purchased / cut and deburr'])
    writer.writerow(['M6 fixed-end captive nut, 5 mm thick',4,8,'Purchased; nominal dimensions illustrated'])
    writer.writerow(['M6 coupling nut, 18 mm long, 10 mm AF',4,8,'DIN 6334; supplier dimension verified'])
    writer.writerow(['M6 hex-head full-thread bolt, 25 mm under-head length',4,8,'Calculated for nominal 335 mm opening, 4 mm nominal head'])
print(PDF/'kallax_filament_visual_assembly_guide.pdf')
