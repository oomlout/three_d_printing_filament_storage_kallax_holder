"""Build catalogue geometry and publish the assembled kit."""
from components.kallax.assembly_cards import ROOT

def main(**kwargs):
    from components.kallax.build import main as build
    records = kwargs.pop("parts", None)
    if records is None and "configuration" not in kwargs:
        from working_oomp_populate import get_options
        import yaml
        records = [yaml.safe_load((ROOT / "parts" / p["id"] / "working.yaml").read_text(encoding="utf-8"))
                   for p in get_options()]
    if records is not None:
        from components.kallax.kit_geometry import export_assembly, export_component, openscad_binary
        openscad = openscad_binary()
        kit, = (record for record in records if record["name"] == "one_cell_kit")
        configuration = kit["oobb_details"]
        expected = {part["id"] for part in configuration["parts"].values() if part.get("printed")}
        children = [record for record in records if record["id"] != kit["id"]]
        if {record["id"] for record in children} != expected:
            raise ValueError("Kit BOM and catalogue print definitions disagree")
        for child in children:
            export_component(ROOT / child["directory"], child, openscad)
        export_assembly(ROOT / kit["directory"], configuration, children, openscad)
        kwargs["configuration"] = configuration
    return build(**kwargs)


if __name__ == "__main__":
    main()
