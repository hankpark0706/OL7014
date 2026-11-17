"""
portfolio_app.py — standalone entry point for the portfolio dashboard.

Used to build a self-contained executable with PyInstaller, so the dashboard can
be run on a machine that has no Python installed:

    pyinstaller --onefile --name Portfolio-Dashboard --paths . portfolio_app.py

(see build_exe.py for the full command). Running this file directly also works.
"""
import os
import sys

# make sure sibling modules (portfolio_core, portfolio_dashboard) are importable,
# both when run normally and when frozen by PyInstaller
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
if getattr(sys, "frozen", False):
    sys.path.insert(0, os.path.dirname(sys.executable))
    sys.path.insert(0, getattr(sys, "_MEIPASS", ""))

import matplotlib

# PORTFOLIO_SMOKE lets us verify a frozen build works without opening a window
_SMOKE = bool(os.environ.get("PORTFOLIO_SMOKE"))
if _SMOKE:
    _backend = "Agg"
elif sys.platform == "darwin":
    _backend = "macosx"        # native macOS GUI — no tkinter needed
else:
    _backend = "TkAgg"         # Windows / Linux
matplotlib.use(_backend, force=True)

import portfolio_dashboard as app         # builds the figure (module-level code)
import matplotlib.pyplot as plt

if _SMOKE:
    app.on_solve_focused(None)            # exercise the scipy/HiGHS solver path
    app.on_new_sample(None)
    print("SMOKE OK")
    sys.exit(0)

plt.show()
