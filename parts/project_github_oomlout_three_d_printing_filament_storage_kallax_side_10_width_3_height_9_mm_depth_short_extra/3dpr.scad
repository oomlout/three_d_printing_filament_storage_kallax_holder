// Dimensions in mm
thickness = 9;
width = 10;
height = 3;

$fn = 50;
pitch = 15;
end_x = (width-1)*pitch/2;
end_y = (height-1)*pitch/2;
bars = height > 5 ? [-end_y, end_y-2*pitch] : [-end_y];

module bar(w,h) {
    hull()
        for (x=[-1,1], y=[-1,1])
            translate([x*(w/2-5),y*(h/2-5),0]) cylinder(r=5,h=thickness);
}
module hole(x,y,r) {
    translate([x,y,-1]) cylinder(r=r,h=thickness+2);
}
difference() {
    union() {
        for (y=bars) translate([0,y,0]) bar(width*pitch-1,14);
        for (x=[-end_x,end_x]) translate([x,0,0]) bar(14,height*pitch-1);
    }
    for (y=bars) {
        for (x=[-end_x:pitch:end_x]) hole(x,y,3.25);
        for (x=[-end_x+pitch/2:pitch:end_x]) hole(x,y,1.8);
    }
    for (x=[-end_x,end_x]) {
        hole(x,end_y,3.25);
        for (i=[0:height-3]) {
            hole(x,-end_y+i*pitch,3.25);
            hole(x,-end_y+(i+0.5)*pitch,1.8);
        }
        for (y=concat(bars,[end_y]))
            translate([x,y,0]) cylinder(r=5.91425,h=5,$fn=6);
    }
}
