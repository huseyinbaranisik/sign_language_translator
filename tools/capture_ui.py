"""Renders the real PyQt5 window (IsaretDiliProjesi/src/arayuz.py) to assets/app-ui.png at 2x, without a camera.

usage: python tools/capture_ui.py        (needs PyQt5; the window is never shown on screen)
"""
import os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("QT_SCALE_FACTOR", "2")
sys.path.insert(0, os.path.join(ROOT, "IsaretDiliProjesi", "src"))

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog
from arayuz import Ui_main_window

app = QApplication(sys.argv)
win = QDialog()
win.setAttribute(Qt.WA_DontShowOnScreen)  # the offscreen platform has no fonts on Windows, so render hidden instead
Ui_main_window().setupUi(win)
win.show()
app.processEvents()
out = os.path.join(ROOT, "assets", "app-ui.png")
win.grab().save(out)
print("->", out)
