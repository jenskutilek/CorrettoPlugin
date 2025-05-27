# MenuTitle: Check Corretto Installation

__doc__ = "Check your Corretto installation and install any missing Python modules."

from GlyphsApp import Message
from vanilla.dialogs import askYesNoCancel

try:
    from jkUnicode import UniInfo  # noqa: F401

    install_jkunicode = False
except ImportError:
    install_jkunicode = True

try:
    from yaml import load  # noqa: F401

    install_yaml = False
except ImportError:
    install_yaml = True

try:
    import brotli  # noqa: F401

    install_brotli = False
except ImportError:
    install_brotli = True

try:
    import zopfli  # noqa: F401

    install_zopfli = False
except ImportError:
    install_zopfli = True


if not any((install_jkunicode, install_yaml, install_brotli, install_zopfli)):
    Message("There should be no problem using Corretto.", title="Everything is fine")

else:
    print("Install jkUnicode:", install_jkunicode)
    print("Install YAML:", install_yaml)
    print("Install brotli (WOFF1):", install_brotli)
    print("Install zopfli (WOFF2):", install_zopfli)
    result = askYesNoCancel(
        "Missing modules detected",
        "Some modules needed for Corretto are missing. Install them now?",
    )

    if result:
        try:
            from corretto.installHelper import installViaPip

            if install_brotli:
                installViaPip("brotli")
            if install_zopfli:
                installViaPip("zopfli")
            if install_jkunicode:
                installViaPip("jkunicode")
            if install_yaml:
                installViaPip("pyyaml")

            Message(
                "Please restart Glyphs to start using Corretto.",
                title="Modules were installed",
            )

        except ImportError:
            Message(
                "Did you install the plugin and restart Glyphs afterwards?",
                title="Corretto plugin not found",
            )
