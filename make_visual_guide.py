"""Compatibility entry point for the current presentation builder."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parent / "presentation/scripts/build.py"), run_name="__main__")
