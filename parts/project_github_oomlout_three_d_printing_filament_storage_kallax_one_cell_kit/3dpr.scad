// Printed parts in installed positions. Use the 3MF for printing.
// project_github_oomlout_three_d_printing_filament_storage_kallax_side_10_width_3_height_9_mm_depth_short_extra
module P1() {
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

}
// project_github_oomlout_three_d_printing_filament_storage_kallax_side_10_width_8_height_9_mm_depth_short_extra
module P2() {
// Dimensions in mm
thickness = 9;
width = 10;
height = 8;

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

}
// project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_99_67_mm_depth_one_end_nut_extra
module P3() {
// Dimensions in mm
thickness = 99.67;
pocket_depth = 5;

$fn = 50;
difference() {
    cylinder(r=7,h=thickness);
    translate([0,0,-1]) cylinder(r=3.25,h=thickness+2);
    cylinder(r=5.91425,h=pocket_depth,$fn=6);
}

}
// project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_67_67_mm_depth_one_end_nut_extra
module P4() {
// Dimensions in mm
thickness = 67.67;
pocket_depth = 5;

$fn = 50;
difference() {
    cylinder(r=7,h=thickness);
    translate([0,0,-1]) cylinder(r=3.25,h=thickness+2);
    cylinder(r=5.91425,h=pocket_depth,$fn=6);
}

}
// project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_18_mm_depth_full_nut_extra
module P5() {
// Dimensions in mm
thickness = 18;
pocket_depth = 18;

$fn = 50;
difference() {
    cylinder(r=7,h=thickness);
    translate([0,0,-1]) cylinder(r=3.25,h=thickness+2);
    cylinder(r=5.91425,h=pocket_depth,$fn=6);
}

}
// project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_11_mm_depth_full_nut_extra
module P6() {
// Dimensions in mm
thickness = 11;
pocket_depth = 11;

$fn = 50;
difference() {
    cylinder(r=7,h=thickness);
    translate([0,0,-1]) cylinder(r=3.25,h=thickness+2);
    cylinder(r=5.91425,h=pocket_depth,$fn=6);
}

}
// project_github_oomlout_three_d_printing_filament_storage_kallax_spacer_1_width_1_height_11_mm_depth_slotted_overlap_extra
module P7() {
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

}
multmatrix([[0,0,1,-167.505],[1,0,0,0],[0,1,0,22],[0,0,0,1]]) P1(); // front_frame_1
multmatrix([[0,0,1,-58.834999999999994],[1,0,0,0],[0,1,0,22],[0,0,0,1]]) P1(); // front_frame_2
multmatrix([[0,0,1,17.835000000000008],[1,0,0,0],[0,1,0,22],[0,0,0,1]]) P1(); // front_frame_3
multmatrix([[0,0,-1,167.505],[-1,0,0,0],[0,1,0,22],[0,0,0,1]]) P1(); // front_frame_4
multmatrix([[0,0,1,-158.505],[1,0,0,-67.5],[0,1,0,37],[0,0,0,1]]) P3(); // front_long_first_0
multmatrix([[0,0,1,-49.834999999999994],[1,0,0,-67.5],[0,1,0,37],[0,0,0,1]]) P4(); // front_centre_0
multmatrix([[0,0,-1,126.505],[1,0,0,-67.5],[0,-1,0,37],[0,0,0,1]]) P3(); // front_long_last_0
multmatrix([[0,0,1,126.505],[1,0,0,-67.5],[0,1,0,37],[0,0,0,1]]) P5(); // front_housing_0
multmatrix([[0,0,1,144.505],[-1,0,0,-67.5],[0,-1,0,37],[0,0,0,1]]) P7(); // front_clip_0
multmatrix([[0,0,1,147.505],[1,0,0,-67.5],[0,1,0,37],[0,0,0,1]]) P6(); // front_nut_cover_0
multmatrix([[0,0,1,-158.505],[1,0,0,67.5],[0,1,0,37],[0,0,0,1]]) P3(); // front_long_first_1
multmatrix([[0,0,1,-49.834999999999994],[1,0,0,67.5],[0,1,0,37],[0,0,0,1]]) P4(); // front_centre_1
multmatrix([[0,0,-1,126.505],[1,0,0,67.5],[0,-1,0,37],[0,0,0,1]]) P3(); // front_long_last_1
multmatrix([[0,0,1,126.505],[1,0,0,67.5],[0,1,0,37],[0,0,0,1]]) P5(); // front_housing_1
multmatrix([[0,0,1,144.505],[-1,0,0,67.5],[0,-1,0,37],[0,0,0,1]]) P7(); // front_clip_1
multmatrix([[0,0,1,147.505],[1,0,0,67.5],[0,1,0,37],[0,0,0,1]]) P6(); // front_nut_cover_1
multmatrix([[0,0,1,-167.505],[1,0,0,187],[0,1,0,59.5],[0,0,0,1]]) P2(); // rear_frame_1
multmatrix([[0,0,1,-58.834999999999994],[1,0,0,187],[0,1,0,59.5],[0,0,0,1]]) P2(); // rear_frame_2
multmatrix([[0,0,1,17.835000000000008],[1,0,0,187],[0,1,0,59.5],[0,0,0,1]]) P2(); // rear_frame_3
multmatrix([[0,0,-1,167.505],[-1,0,0,187],[0,1,0,59.5],[0,0,0,1]]) P2(); // rear_frame_4
multmatrix([[0,0,1,-158.505],[1,0,0,119.5],[0,1,0,112],[0,0,0,1]]) P3(); // rear_long_first_0
multmatrix([[0,0,1,-49.834999999999994],[1,0,0,119.5],[0,1,0,112],[0,0,0,1]]) P4(); // rear_centre_0
multmatrix([[0,0,-1,126.505],[1,0,0,119.5],[0,-1,0,112],[0,0,0,1]]) P3(); // rear_long_last_0
multmatrix([[0,0,1,126.505],[1,0,0,119.5],[0,1,0,112],[0,0,0,1]]) P5(); // rear_housing_0
multmatrix([[0,0,1,144.505],[-1,0,0,119.5],[0,-1,0,112],[0,0,0,1]]) P7(); // rear_clip_0
multmatrix([[0,0,1,147.505],[1,0,0,119.5],[0,1,0,112],[0,0,0,1]]) P6(); // rear_nut_cover_0
multmatrix([[0,0,1,-158.505],[1,0,0,254.5],[0,1,0,112],[0,0,0,1]]) P3(); // rear_long_first_1
multmatrix([[0,0,1,-49.834999999999994],[1,0,0,254.5],[0,1,0,112],[0,0,0,1]]) P4(); // rear_centre_1
multmatrix([[0,0,-1,126.505],[1,0,0,254.5],[0,-1,0,112],[0,0,0,1]]) P3(); // rear_long_last_1
multmatrix([[0,0,1,126.505],[1,0,0,254.5],[0,1,0,112],[0,0,0,1]]) P5(); // rear_housing_1
multmatrix([[0,0,1,144.505],[-1,0,0,254.5],[0,-1,0,112],[0,0,0,1]]) P7(); // rear_clip_1
multmatrix([[0,0,1,147.505],[1,0,0,254.5],[0,1,0,112],[0,0,0,1]]) P6(); // rear_nut_cover_1
