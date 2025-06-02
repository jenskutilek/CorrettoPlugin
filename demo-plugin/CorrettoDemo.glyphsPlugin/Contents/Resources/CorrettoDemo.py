from __future__ import annotations

from corretto.plugins import CorrettoPlugin

# The class of your Corretto plugin must be called Plugin and must subclass
# `corretto.plugins.CorrettoPlugin`.


class Plugin(CorrettoPlugin):

    # The configuration will be read from this Custom Parameter if present:
    cpkey = "de.kutilek.corretto.demo"

    def parse_config(self, config: str) -> str:
        # Our Custom Parameter's value is always read as a string.
        # If necessary, you can parse and convert the value into a format your
        # plugin understands.

        # If you don't need to do any processing, you can also delete the `parse_config`
        # method.

        # In this example, we just return the config as is.
        return config

    def process(self) -> bool:
        # Do the actual processing of the font.

        # If your plugin needs configuration via a Custom Parameter, but it is not
        # configured, return `False`.
        # if self.config is None:
        #     return False

        # The contents of your Custom Parameter is stored here:
        print(f"CorrettoDemo config: {self.config}")

        # You can access the `fontTools.ttLib.TTFont` object of the exported font in
        # `ttfont`:
        table_tags = self.ttfont.keys()
        print(f"The SFNT file has {len(table_tags)} tables: {table_tags}")

        # Also, its full file path is available:
        print(f"It is saved at '{self.ttfont_path}'.")

        # In case you need to add information from the `GSInstance` that describes your
        # font, it is also available:
        print(f"The font was generated from instance {self.gsinstance}")

        # As are the `GSFont` and its file path:
        print(
            f"It belongs to the font {self.gsfont} which is saved at {self.gsfont_path}"
        )

        # If you want to work around bugs in certain Glyphs versions, you can check the
        # build number:
        print(f"Presented by Glyphs build {self.app_build}")

        # If your plugin has modified the font, return True.
        return False
