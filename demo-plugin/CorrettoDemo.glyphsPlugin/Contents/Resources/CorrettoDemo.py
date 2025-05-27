from __future__ import annotations

from corretto.plugins import CorrettoPlugin


class Plugin(CorrettoPlugin):
    # The configuration will be read from this Custom Parameter if present:
    cpkey = "de.kutilek.corretto.demo"

    def parse_config(self, config: str) -> str:
        # A Custom Parameter's value is always read as a string.
        # If necessary, you can parse and convert the value into a format your
        # plugin understands.
        return config

    def process(self) -> bool:
        # If the plugin is not configured, return False.
        if self.config is None:
            return False

        # Just print some stats
        print(self.ttfont)
        print(self.ttfont_path)
        print(self.gsinstance)
        print(self.gsfont)
        print(self.gsfont_path)

        # If your plugin has modified the font, return True.
        return False
