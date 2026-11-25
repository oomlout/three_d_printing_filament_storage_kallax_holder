// Dimensions in mm
thickness = 11;
overlap = 8;

$fn = 96;
neck = thickness-overlap;
difference() {
    cylinder(h=thickness,r=9);
    translate([0,0,-0.1]) cylinder(h=thickness+0.2,r=3.25);
    translate([-2.9,0,-0.1]) cube([5.8,12,thickness+0.2]);
    translate([0,0,neck]) cylinder(h=overlap+0.1,r=7.3);
    translate([-6.9,0,neck]) cube([13.8,12,overlap+0.1]);
}
