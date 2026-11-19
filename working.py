"""Regenerate documentation from the current production STL files."""
import argparse

def main(**kwargs):
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
