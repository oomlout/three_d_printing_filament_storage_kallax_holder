"""Recreate the one-cell kit from its Python definitions."""
import working


def main(**kwargs):
    from components.kallax.print_project import validate_slice
    assembly = working.run(**kwargs)
    validate_slice(assembly.parent)
    return assembly.parent


if __name__ == "__main__":
    main()
