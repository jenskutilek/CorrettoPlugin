from __future__ import annotations

import objc
from GlyphsApp.plugins import GeneralPlugin


class CorrettoDemoPlugin(GeneralPlugin):

    @objc.python_method
    def __file__(self):
        """Please leave this method unchanged"""
        return __file__
