<!-- BANNER -->

Allows you to insert **syntax-highlighted code snippets** into your notes:

![](https://raw.githubusercontent.com/glutanimate/syntax-highlighting/master/screenshots/screenshot_python.png)

<!-- CHANGELOG -->

### USAGE

1. Open the Add Note window in Anki.
2. Compose your code snippet in your favorite text editor.
3. Copy the code to the clipboard (e.g. Ctrl+C)
4. Move the cursor to to the field you want to insert your code snippet into
5. In the top right corner of the editing window there should be a new Thunderbolt icon with a dropdown.
6. Choose the language your snippet is written in, and click the Thunderbolt / use it's associated hotkey (default: `Alt+S`).
7. Anki will copy your syntax highlighted snippet to the field

Alternatively, you can compose your code directly in Anki, highlight it, and then click the lightning button. But generally it is much more convenient to use a dedicated code editor with monospaced fonts and proper syntax highlighting.

The add-on will automatically remember the last programming language you chose, even after restarting Anki.

### CONFIGURATION

**Basic**

Currently there are four configuration options, available from Anki's main screen through *Tools* → *Syntax Highlighting Options*:

- **Line numbers** (default: true): Whether or not to include line numbers in the highlighted code
- **Center code fragments** (default: true): Whether or not to automatically center the code in the field
- **Use CSS classes** (default: false): Whether or not to use CSS classes instead of inline HTML styles for syntax highlighting.

    - Using css classes allows you more customization, and results in a smaller database size, but you'll need to manually adjust the styling, so it's only recommended for advanced users. You will find a selection of CSS styles that you can use in the [documentation on GitHub](https://github.com/glutanimate/syntax-highlighting/blob/master/docs/css.md). 
    - For proper styling of *reviews* you need to include the relevant CSS styles in the Styling section of the card templates of every note type. At the time of the release of this add-on Anki can load css from an external file in your media folder if you use  a line like `@import url("_styles_for_syntax_highlighting.css");`, for details see [here](https://apps.ankiweb.net/docs/manual.html#media18). But loading css from an external file is not documented in the manual. It might break in the future.
    - For proper styling of the editor component in the *Add* window and at the bottom of the *Browser* window you need the add-on [Customize Editor Stylesheet](https://ankiweb.net/shared/info/1215991469) and copy the relevant styles to the file `_editor.css` file in your media collection. Add-ons don't work on AnkiMobile for iOS or Ankidroid for Android. If you use the css option you won't have syntax highlighting in the editor component.

- **Default to last language used per deck** (default: true): Whether or not to remember the last programming language for each deck individually

Please note that changes in the configuration will only affect new notes.

**Advanced**

*Syntax Highlighting* also comes with a number of advanced options. These can be edited by either using Anki 2.1's inbuilt add-on configuration screen (*Tools* → *Add-ons* → select *Syntax Highlighting* → click on *Config*) or by manually editing the corresponding config keys in `syntax_highlighting/meta.json` in Anki's add-on folder (Anki 2.0) [the config.json file contains the default values and **should not be modified**.]

The following options may be customized:

- `hotkey` [string]: Add-on invocation hotkey. Default: `Alt+S`
- `limitToLags` [list]: List of programming languages to limit combobox menu to. Default: `[]` (i.e. no limit). Example: `["Python", "Java", "JavaScript"]`.
- `style` [string]: Pre-defined [pygments style](https://help.farbox.com/pygments.html) to use for inline styling of code (not applicable to CSS mode). Default: `default`. Example: `monokai`.

These advanced settings do not sync and require a restart to apply.

<!-- SUPPORT -->

### CREDITS AND LICENSE

*Copyright © 2012-2015 [Tiago Barroso](https://github.com/tmbb)*
*Copyright © 2015 [Tim Rae](https://github.com/timrae)*
*Copyright © 2018-2019 [Aristotelis P.](https://glutanimate.com/)  (Glutanimate)*

*Syntax Highlighting* is based on [*Syntax Highlighting for Code*](https://github.com/tmbb/SyntaxHighlight) by [Tiago Barroso](https://github.com/tmbb). All credit for the original idea and implementation goes to him. A major thanks is also due to [Tim Rae](https://github.com/timrae), who extended the original add-on with CSS support.

The present fork and update to Anki 2.1 was made possible through the generous support of a fellow Anki user who would like to remain anonymous.

Licensed under the _GNU AGPLv3_, extended by a number of additional terms. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY. For more information on the license please see the [LICENSE file](https://github.com/glutanimate/syntax-highlighting/blob/master/LICENSE) accompanying this add-on. The source code is available on [![GitHub icon](https://glutanimate.com/logos/github.svg) GitHub](https://github.com/glutanimate/syntax-highlighting). Pull requests and other contributions are welcome!

<!-- RESOURCES -->

<!-- FUNDING -->
