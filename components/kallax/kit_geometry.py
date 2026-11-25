"""Self-contained OpenSCAD sources for the released KALLAX print profiles."""
from pathlib import Path
from tempfile import TemporaryDirectory
import shutil
import subprocess

from .instances import define_instances


# The legacy frames use 5 mm corner radii. These dimensions are fixed here
# because the shared OOBB rounded-plate defaults changed after their release.
FRAME = """
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
"""

SLEEVE = """
$fn = 50;
difference() {
    cylinder(r=7,h=thickness);
    translate([0,0,-1]) cylinder(r=3.25,h=thickness+2);
    cylinder(r=5.91425,h=pocket_depth,$fn=6);
}
"""

CLIP = """
$fn = 96;
neck = thickness-overlap;
difference() {
    cylinder(h=thickness,r=9);
    translate([0,0,-0.1]) cylinder(h=thickness+0.2,r=3.25);
    translate([-2.9,0,-0.1]) cube([5.8,12,thickness+0.2]);
    translate([0,0,neck]) cylinder(h=overlap+0.1,r=7.3);
    translate([-6.9,0,neck]) cube([13.8,12,overlap+0.1]);
}
"""


def component_source(record):
    params = record["kwargs"]
    length = params["thickness"]
    header = f"// Dimensions in mm\nthickness = {length};\n"
    if record["name"] == "side":
        return header + f"width = {params['width']};\nheight = {params['height']};\n" + FRAME
    if params["extra"] == "slotted_overlap":
        return header + f"overlap = {params['overlap']};\n" + CLIP
    pocket = 5 if params["extra"] == "one_end_nut" else length
    return header + f"pocket_depth = {pocket};\n" + SLEEVE


def assembly_source(configuration, children):
    """Embed each child definition once so the assembled model travels alone."""
    parts = configuration["parts"]
    catalogue = {child["id"]: child for child in children}
    lines = ["// Printed parts in installed positions. Use the 3MF for printing."]
    for key, part in parts.items():
        if part.get("printed"):
            source = component_source(catalogue[part["id"]])
            lines.extend([f"// {part['id']}", f"module {key}() {{", source, "}"])
    for item in define_instances():
        key = item["part"]
        if not parts[key].get("printed"):
            continue
        # A cyclic XYZ rotation puts the local extrusion direction along the rail.
        sx, sy, sz = 1, 1, 1
        if key == "P7":
            sy, sz = -1, -1
        elif item["reverse"]:
            sx = -1
            if key in ("P1", "P2"):
                sy = -1
            else:
                sz = -1
        x, y, z = item["pos"]
        lines.append(f"multmatrix([[0,0,{sx},{x}],[{sy},0,0,{y}],[0,{sz},0,{z}],[0,0,0,1]]) {key}(); // {item['name']}")
    return "\n".join(lines) + "\n"


def export_component(folder, record, executable):
    import trimesh

    # Compile and validate both artifacts before replacing the catalogue files.
    with TemporaryDirectory(dir=folder) as temporary:
        source = Path(temporary) / "3dpr.scad"
        mesh = source.with_suffix(".stl")
        source.write_text(component_source(record), encoding="utf-8")
        subprocess.run([executable, "--export-format", "binstl", "-o", str(mesh), str(source)], check=True)
        solid = trimesh.load_mesh(mesh)
        if not solid.is_volume or solid.body_count != 1:
            raise ValueError(f"Invalid print mesh for {record['id']}")
        source.replace(folder / source.name)
        mesh.replace(folder / mesh.name)


def export_assembly(folder, configuration, children, executable):
    with TemporaryDirectory() as temporary:
        source = Path(temporary) / "3dpr.scad"
        source.write_text(assembly_source(configuration, children), encoding="utf-8")
        # Resolve every module in isolation, as when opening a standalone download.
        subprocess.run([executable, "--hardwarnings", "-o", str(source.with_suffix(".csg")), str(source)], check=True)
        shutil.copyfile(source, folder / source.name)


def openscad_binary():
    path = shutil.which("openscad.com") or shutil.which("openscad")
    if not path:
        raise FileNotFoundError("The make-all action requires OpenSCAD on PATH.")
    return path
