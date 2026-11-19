"""Compatibility entry point for the current versioned documentation builder."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parent / "working.py"), run_name="__main__")
