"""Production-mesh documentation stage; retains the existing printable geometry."""
import copy

def main(**kwargs):
    from components.kallax.build import main as build
    kwargs=copy.deepcopy(kwargs)
    kwargs.setdefault('render',True)
    return build(**kwargs)
