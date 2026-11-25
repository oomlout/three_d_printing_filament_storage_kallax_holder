// Dimensions in mm
thickness = 18;
pocket_depth = 18;

$fn = 50;
difference() {
    cylinder(r=7,h=thickness);
    translate([0,0,-1]) cylinder(r=3.25,h=thickness+2);
    cylinder(r=5.91425,h=pocket_depth,$fn=6);
}
