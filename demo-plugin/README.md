# Demo Plugin For Corretto

1. To install, drag `CorrettoDemo.glyphsPlugin` onto the Glyphs app icon in your dock.
2. Restart Glyphs.
3. Add `CorrettoDemo` to your Corretto configuration file `~/Library/Application Support/Glyphs 3/global.correttoconfig.yaml`:

    ```yaml
    corretto:
        plugins:
            - module: corretto.plugins.MathTable
            - module: corretto.plugins.MergeTTX
            - module: corretto.plugins.FixedPitch
            - module: corretto.plugins.GaspTable
            - module: corretto.plugins.DeltaBase
            - module: corretto.plugins.MaxpStack
            - module: corretto.plugins.HeadTable
            - module: corretto.plugins.VariableFontMetrics
            - module: corretto.plugins.Save
            - module: corretto.plugins.SaveCFF2Static
            - module: corretto.plugins.SaveTTX
            - module: corretto.plugins.Webfonts
            - module: CorrettoDemo # New!
    ```

    The name of the module must match its file name inside the plugin’s _Resources_
    folder: `CorrettoDemo.glyphsPlugin/Contents/Resources/CorrettoDemo.py` →
    `- module: CorrettoDemo`.

    You can add it at the end, or wherever you like. If your own plugin actually modifies
    the exported font, you must list it before the `corretto.plugins.Save` plugin so the
    modifications will be permanently applied to the font file.

4. Copy and paste this Custom Parameter to your Glyphs file (Font Info – Font) to enable
   post-processing with Corretto:
    ```plist
    {
      customParameters = (
        {
          name = de.kutilek.corretto.active;
          value = "1";
        }
      );
    }
    ```
5. Export your font. You will see some stats printed in the Output Pane of the Macro
   Panel.

Something like this should be printed to the Output Pane:

```
Corretto working on ~/Schriften/MyFont/fonts/MyFont-Regular.otf'.
CorrettoDemo config: None
The SFNT file has 12 tables: ['GlyphOrder', 'head', 'hhea', 'maxp', 'OS/2', 'name', 'cmap', 'post', 'CFF ', 'GDEF', 'GPOS', 'hmtx']
It is saved at '~/Schriften/MyFont/fonts/MyFont-Regular.otf'.
The font was generated from instance <GSInstance "Regular" (0.0)>
It belongs to the font <GSFont "MyFont" v1.0 with 2 masters and 2 instances> which is saved at ~/Schriften/MyFont/MyFont.glyphs
Presented by Glyphs build 3414.0
```
