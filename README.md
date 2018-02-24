## Code Syntax Highlighter Add-on for Anki

Allows you to insert syntax-highlighted code snippets into the spaced-repetition flashcard app [Anki](https://apps.ankiweb.net/).

### Table of Contents

<!-- MarkdownTOC -->

- [Screenshots](#screenshots)
- [Installation](#installation)
- [Documentation](#documentation)
- [License and Credits](#license-and-credits)

<!-- /MarkdownTOC -->

### Screenshots

![](screenshots/screenshot_python.png)

![](screenshots/screenshot_java.png)

### Installation

**AnkiWeb**

[Link to the add-on on AnkiWeb](https://ankiweb.net/shared/info/not_available_yet)

**Manual installation**

*Anki 2.0*

1. Go to *Tools* → *Add-ons* → *Open add-ons folder*
2. Find and delete `Code Syntax Highlighter.py` and `syntax_highlighter` if they already exist
3. Download and extract the latest Anki 2.0 add-on release from the [releases tab](https://github.com/Glutanimate/syntax-highlighter/releases)
4. Move `Code Syntax Highlighter.py` and `syntax_highlighter` into the add-ons folder
5. Restart Anki

*Anki 2.1*

1. Go to *Tools* → *Add-ons* → *Open add-ons folder*
2. See if the `syntax_highlighter` folder already exists
3. If you would like to keep your settings thus far: Find the `meta.json` file contained within and copy it to a safe location.
4. Proceed to delete  the `syntax_highlighter` folder
3. Download and extract the latest Anki 2.1 add-on release from the [releases tab](https://github.com/Glutanimate/syntax-highlighter/releases)
4. Move the new `syntax_highlighter` folder into the add-ons directory
5. Optional: Place the `meta.json` file back in the directory if you created a copy beforehand.
5. Restart Anki

### Documentation

For further information on the use of this add-on please check out [the original add-on description](docs/description.md).

### License and Credits

*Copyright © 2012-2015 [Tiago Barroso](https://github.com/tmbb)*

*Copyright © 2015 [Tim Rae](https://github.com/timrae)*

*Copyright © 2018 [Aristotelis P.](https://glutanimate.com/)*

*Code Syntax Highlighter* is based on [*Syntax Highlighting for Code*](https://github.com/tmbb/SyntaxHighlight) by [Tiago Barroso](https://github.com/tmbb). All credit for the original add-on goes to him. A major thanks is also due for [Tim Rae](https://github.com/timrae), who extended the original add-on with CSS support.

The present fork and update to Anki 2.1 was made possible through the generous support of a fellow Anki user who would like to remain anonymous.

*Code Syntax Highlighter* ships with the following third-party open-source software:

- [Pygments](http://pygments.org/) v2.2.0. Copyright (c) 2006-2017 by the Pygments Team. Licensed under the BSD license.

This program is free software: you can redistribute it and/or modify it under the terms of the [GNU Affero General Public License](https://www.gnu.org/licenses/agpl.html) as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. 

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
