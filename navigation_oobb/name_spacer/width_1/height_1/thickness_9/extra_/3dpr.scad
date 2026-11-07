$fn = 50;


difference() {
	union() {
		cylinder(h = 9, r = 7.0000000000);
	}
	union() {
		translate(v = [0, 0, -100]) {
			cylinder(h = 200, r = 3.2500000000);
		}
		translate(v = [0, 0, -100]) {
			cylinder(h = 200, r = 1.8000000000);
		}
	}
}