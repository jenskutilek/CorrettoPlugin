from __future__ import annotations

from pathlib import Path
from sys import path, version_info

py_ok = False
if version_info.major == 3:
    if version_info.minor in (10, 11, 12, 13, 14):
        cor_path = Path(__file__).parent / f"corretto3{version_info.minor}.zip"
        path.append(str(cor_path))
        py_ok = True

if not py_ok:
    from GlyphsApp import Message

    Message(
        f"Python version {version_info.major}.{version_info.minor} "
        "is not supported by Corretto."
    )

import objc
from corretto import Corretto
from GlyphsApp import Glyphs
from GlyphsApp.plugins import GeneralPlugin


class CorrettoPlugin(GeneralPlugin):
    @objc.python_method
    def settings(self):
        self.name = Glyphs.localize({"en": "Corretto"})

    @objc.python_method
    def start(self):
        Corretto.startup()

    @objc.python_method
    def __file__(self):
        """Please leave this method unchanged"""
        return __file__
