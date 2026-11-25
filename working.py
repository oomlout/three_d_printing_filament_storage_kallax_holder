"""Regenerate documentation from the current production STL files."""
import argparse

def run(**kwargs):
    """Run the same populate -> catalogue -> SCAD sequence as other OOBB kits."""
    import working_oomp_populate
    import working_oomp
    import working_scad
    options = working_oomp_populate.main() if kwargs.pop("run_oomp_populate", True) else None
    records = None
    if kwargs.pop("run_oomp", True):
        selection = {} if options is None else {"part_ids": [option["id"] for option in options]}
        records = working_oomp.main(**selection)
    if kwargs.pop("run_scad", True):
        return working_scad.main(parts=records, **kwargs)
    return records if records is not None else options


def main(**kwargs):
    if any(flag in kwargs for flag in ("run_oomp_populate", "run_oomp", "run_scad")):
        return run(**kwargs)
    import working_oomp
    kwargs.setdefault('assembly_documentation', True)
    return working_oomp.main(**kwargs)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--assembly-only', action='store_true', help='Rebuild instructions from current production meshes')
    parser.add_argument('--no-renders', action='store_true', help='Recompose using hash-validated cached diagrams')
    parser.add_argument('--blender', help='Blender executable; defaults to PATH')
    args = parser.parse_args()
    main(render=not args.no_renders, blender=args.blender)
