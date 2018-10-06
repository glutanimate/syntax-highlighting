
Allows you to insert **syntax-highlighted code snippets** into your notes.

**SCREENSHOT**

![](https://raw.githubusercontent.com/glutanimate/syntax-highlighting/master/screenshots/screenshot_python.png)

**RELEASE LOG**

- 2018-10-06: v2.0.1 – Case-insensitive language sorting
- 2018-08-16: **v2.0.0** – Initial release of this fork
- 2015-12-25: CSS class option implemented by Tim Rae
- 2015-11-20: Last updated release of the original add-on on AnkiWeb
- 2012: **v1.0.0**? – Initial release by Tiago Barroso

**LATEST CHANGES AND NEWS**

*2018-08-16* **v2.0.0**

This is the first public release of my fork of Tiago Barroso's *Syntax Highlighting for Code* add-on. I would like to extend my heartfelt gratitude to all of what he has done for the Anki community over the years.

This update is meant to carry on his legacy by adding Anki 2.1 support, implementing some long-requested features, and refactoring major parts of the codebase. All of this was made possible through the generous support of a fellow Anki user who would like to remain anonymous.

An overview of the most important changes in this release follows below:

- **New**: Anki 2.1 compatibility
- **New**: Option to apply syntax highlighting via CSS (thanks to [Tim Rae](https://github.com/timrae/SyntaxHighlight)!)
- **New**: Ability to customize language selection and hotkey
- **New**: Ability to customize [syntax highlighting theme](https://help.farbox.com/pygments.html)
- **New**: Upgraded pygments from v1.6 to v2.2.0. This is a [major jump](http://pygments.org/docs/changelog/#version-2-2-0) and should come with a lot of added functionality in terms of supported languages and language features
- **Fixed**: Position options dialog correctly
- **Fixed**: Various improvements and bug fixes (e.g. the ImportErrors and KeyErrors frequently reported in earlier reviews)

**USAGE**

1. Open the Add Note window in Anki.
2. Compose your code snippet in your favorite text editor.
3. Copy the code to the clipboard (e.g. Ctrl+C)
4. Move the cursor to to the field you want to insert your code snippet into
5. In the top right corner of the editing window there should be a new Thunderbolt icon with a dropdown.
6. Choose the language your snippet is written in, and click the Thunderbolt / use it's associated hotkey (default: `Alt+S`).
7. Anki will copy your syntax highlighted snippet to the field

Alternatively, you can compose your code directly in Anki, highlight it, and then click the lightning button. But generally it is much more convenient to use a dedicated code editor with monospaced fonts and proper syntax highlighting.

The add-on will automatically remember the last programming language you chose, even after restarting Anki.

**CONFIGURATION**

**Basic**

Currently there are four configuration options, available from Anki's main screen through *Tools* → *Syntax Highlighting Options*:

- **Line numbers** (default: true): Whether or not to include line numbers in the highlighted code
- **Center code fragments** (default: true): Whether or not to automatically center the code in the field
- **Use CSS classes** (default: false): Whether or not to use CSS classes instead of inline styles for syntax highlighting.

    Using css classes allows you more customization, and results in a smaller database size, but you'll need to manually include a styling sheet in every note type, so it's only recommended for advanced users. You will find a selection of CSS styles that you can include in your card templates in the [documentation on GitHub](https://github.com/glutanimate/syntax-highlighting/blob/master/docs/css.md).

- **Default to last language used per deck** (default: true): Whether or not to remember the last programming language for each deck individually

Please note that changes in the configuration will only affect new notes.

**Advanced**

*Syntax Highlighting* also comes with a number of advanced options. These can be edited by either using Anki 2.1's inbuilt add-on configuration screen (*Tools* → *Add-ons* → select *Syntax Highlighting* → click on *Config*) or by manually editing the corresponding config keys in `syntax_highlighting/meta.json` in Anki's add-on folder (Anki 2.0) [the config.json file contains the default values and **should not be modified**.]

The following options may be customized:

- `hotkey` [string]: Add-on invocation hotkey. Default: `Alt+S`
- `limitToLags` [list]: List of programming languages to limit combobox menu to. Default: `[]` (i.e. no limit). Example: `["Python", "Java", "JavaScript"]`.
- `style` [string]: Pre-defined [pygments style](https://help.farbox.com/pygments.html) to use for inline styling of code (not applicable to CSS mode). Default: `default`. Example: `monokai`.

These advanced settings do not sync and require a restart to apply.

**SUPPORT**

Please **do not report issues or bugs in the review section below**. I can only reply to your reviews in a limited fashion, so this is not a good way to strike up a dialog and track issues down. Instead, please report all issues you encounter either by creating a bug report on [GitHub](https://github.com/glutanimate/syntax-highlighting/issues), or by posting a new thread on the [Anki add-on support forums](https://anki.tenderapp.com/discussions/add-ons). Please make sure to include the name of the affected add-on in your report title when you do so.

**CREDITS AND LICENSE**

*Copyright © 2012-2015 [Tiago Barroso](https://github.com/tmbb)*
*Copyright © 2015 [Tim Rae](https://github.com/timrae)*
*Copyright © 2018 [Aristotelis P.](https://glutanimate.com/)*

*Syntax Highlighting* is based on [*Syntax Highlighting for Code*](https://github.com/tmbb/SyntaxHighlight) by [Tiago Barroso](https://github.com/tmbb). All credit for the original idea and implementation goes to him. A major thanks is also due to [Tim Rae](https://github.com/timrae), who extended the original add-on with CSS support.

The present fork and update to Anki 2.1 was made possible through the generous support of a fellow Anki user who would like to remain anonymous.

Licensed under the [GNU AGPLv3](https://www.gnu.org/licenses/agpl.html). The code for this add-on is available on [![GitHub icon](https://glutanimate.com/logos/github.svg) GitHub](https://github.com/glutanimate/syntax-highlighting). For more information on the licensing terms and other software shipped with this package please check out the [README](https://github.com/glutanimate/syntax-highlighting#credits).

**MORE RESOURCES**

A lot of my add-ons were commissioned by other Anki users. Please feel free to reach out to me if you would like to hire my services for any Anki-related development work (writing an add-on for you, converting existing ones to Anki 2.1, implementing a specific feature): ![Email icon](https://glutanimate.com/logos/email.svg) <em>ankiglutanimate [αt] gmail .com</em>. 

Want to stay up-to-date with my latest add-on releases and updates? Feel free to follow me on Twitter: [![Twitter bird](https://glutanimate.com/logos/twitter.svg)@Glutanimate](https://twitter.com/glutanimate)

New to Anki? Make sure to check out my YouTube channel where I post weekly tutorials on Anki add-ons and related topics: [![YouTube playbutton](https://glutanimate.com/logos/youtube.svg) / Glutanimate](https://www.youtube.com/c/glutanimate)

============================================

**SUPPORT THIS ADD-ON**

Writing, supporting, and maintaining Anki add-ons like these takes a lot of time and effort. If *Syntax Highlighting* has been a valuable asset in your studies, please consider using one of the buttons below to support my efforts by buying me a **coffee**, **sandwich**, **meal**, or anything else you'd like:

![](https://glutanimate.com/logos/paypal.svg)        [![](https://glutanimate.com/logos/contrib_btnsw_coffee.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=4FT9NG3NJMY4U&on0=Project&os0=syntax-highlighting "Buy me a coffee ☺")    [![](https://glutanimate.com/logos/contrib_btnsw_sandwich.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YKSP7QF45Y7SJ&on0=Project&os0=syntax-highlighting "Buy me a burger 😊")    [![](https://glutanimate.com/logos/contrib_btnsw_meal.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=MVDM6JAL2R5JA&on0=Project&os0=syntax-highlighting "Buy me a meal 😄")    [![](https://glutanimate.com/logos/contrib_btnsw_custom.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=EYNV4ECSKBGE4&on0=Project&os0=syntax-highlighting "Contribute a custom amount ☺")

**New**: I also have a Patreon now! If you would like to support my work while also receiving some exclusive add-ons and other goodies, please do check it out!:

[![](https://glutanimate.com/logos/patreon_button.svg)](https://www.patreon.com/glutanimate "Support me on Patreon 😄")

Each and every contribution is greatly appreciated and will help me maintain and improve *Syntax Highlighting* as time goes by!