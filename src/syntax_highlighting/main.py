# -*- coding: utf-8 -*-

"""
This file is part of the Syntax Highlighting add-on for Anki.

Main Module, hooks add-on methods into Anki.

Copyright: (c) 2012-2015 Tiago Barroso <https://github.com/tmbb>
           (c) 2015 Tim Rae <https://github.com/timrae>
           (c) 2018 Glutanimate <https://glutanimate.com/>

License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>
"""

from __future__ import unicode_literals

import os
import sys
import re

from .consts import *  # import addon_path
# always use shipped pygments library
# FIXME: properly vendorize pygments, lest we interfere with
# other add-ons that might be shipping their own pygments
sys.path.insert(0, os.path.join(addon_path, "libs"))

from pygments import highlight
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound

from aqt.qt import *
from aqt import mw
from aqt.editor import Editor
from aqt.utils import showWarning
from anki.utils import json
from anki.hooks import addHook, wrap

from .config import local_conf

if anki21:
    string = str
else:
    import string


HOTKEY = local_conf["hotkey"]
STYLE = local_conf["style"]
LIMITED_LANGS = local_conf["limitToLangs"]

# This code sets a correspondence between:
#  The "language names": long, descriptive names we want
#                        to show the user AND
#  The "language aliases": short, cryptic names for internal
#                          use by HtmlFormatter
LANGUAGES_MAP = {lex[0]: lex[1][0] for lex in get_all_lexers()}


ERR_LEXER = ("<b>Error</b>: Selected language not found.<br>"
            "If you set a custom lang selection please make sure<br>"
            "you typed all list entries correctly.")

ERR_STYLE = ("<b>Error</b>: Selected style not found.<br>"
            "If you set a custom style please make sure<br>"
            "you typed it correctly.")


# Misc

def showError(msg, parent):
    showWarning(msg, title="Syntax Highlighting Error", parent=parent)

# Synced options and corresponding dialogs

def get_deck_name(mw):
    deck_name = None
    try:
        deck_name = mw.col.decks.current()['name']
    except AttributeError:
        # No deck opened?
        deck_name = None
    return deck_name


def get_default_lang(mw):
    addon_conf = mw.col.conf['syntax_highlighting_conf']
    lang = addon_conf['lang']
    if addon_conf['defaultlangperdeck']:
        deck_name = get_deck_name(mw)
        if deck_name and deck_name in addon_conf['deckdefaultlang']:
            lang = addon_conf['deckdefaultlang'][deck_name]
    return lang


def set_default_lang(mw, lang):
    addon_conf = mw.col.conf['syntax_highlighting_conf']
    addon_conf['lang'] = lang  # Always update the overall default
    if addon_conf['defaultlangperdeck']:
        deck_name = get_deck_name(mw)
        if deck_name:
            addon_conf['deckdefaultlang'][deck_name] = lang


class SyntaxHighlightingOptions(QDialog):
    def __init__(self, mw):
        super(SyntaxHighlightingOptions, self).__init__()
        self.mw = mw
        self.addon_conf = None
        self.setupUi()

    def switch_linenos(self):
        linenos_ = self.addon_conf['linenos']
        self.addon_conf['linenos'] = not linenos_

    def switch_centerfragments(self):
        centerfragments_ = self.addon_conf['centerfragments']
        self.addon_conf['centerfragments'] = not centerfragments_

    def switch_defaultlangperdeck(self):
        defaultlangperdeck_ = self.addon_conf['defaultlangperdeck']
        self.addon_conf['defaultlangperdeck'] = not defaultlangperdeck_

    def switch_cssclasses(self):
        cssclasses_ = self.addon_conf['cssclasses']
        self.addon_conf['cssclasses'] = not cssclasses_

    def setupUi(self):
        self.addon_conf = self.mw.col.conf['syntax_highlighting_conf']

        linenos_label = QLabel('<b>Line numbers</b>')
        linenos_checkbox = QCheckBox('')
        linenos_checkbox.setChecked(self.addon_conf['linenos'])
        linenos_checkbox.stateChanged.connect(self.switch_linenos)

        center_label = QLabel('<b>Center code fragments</b>')
        center_checkbox = QCheckBox('')
        center_checkbox.setChecked(self.addon_conf['centerfragments'])
        center_checkbox.stateChanged.connect(self.switch_centerfragments)

        cssclasses_label = QLabel('<b>Use CSS classes</b>')
        cssclasses_checkbox = QCheckBox('')
        cssclasses_checkbox.setChecked(self.addon_conf['cssclasses'])
        cssclasses_checkbox.stateChanged.connect(self.switch_cssclasses)

        defaultlangperdeck_label = QLabel(
            '<b>Default to last language used per deck</b>')
        defaultlangperdeck_checkbox = QCheckBox('')
        defaultlangperdeck_checkbox.setChecked(
            self.addon_conf['defaultlangperdeck'])
        defaultlangperdeck_checkbox.stateChanged.connect(
            self.switch_defaultlangperdeck)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(linenos_label, 0, 0)
        grid.addWidget(linenos_checkbox, 0, 1)
        grid.addWidget(center_label, 1, 0)
        grid.addWidget(center_checkbox, 1, 1)
        grid.addWidget(cssclasses_label, 2, 0)
        grid.addWidget(cssclasses_checkbox, 2, 1)
        grid.addWidget(defaultlangperdeck_label, 3, 0)
        grid.addWidget(defaultlangperdeck_checkbox, 3, 1)

        self.setLayout(grid)

        self.setWindowTitle('Syntax Highlighting Options')


def onOptionsCall(mw):
    """Call settings dialog"""
    dialog = SyntaxHighlightingOptions(mw)
    dialog.exec_()


options_action = QAction("Syntax Highlighting Options ...", mw)
options_action.triggered.connect(lambda _, o=mw: onOptionsCall(o))
mw.form.menuTools.addAction(options_action)


# Highlighter initialization


def init_highlighter(ed, *args, **kwargs):
    # Get the last selected language (or the default language if the user
    # has never chosen any)
    previous_lang = get_default_lang(mw)
    ed.codeHighlightLangAlias = LANGUAGES_MAP.get(previous_lang, "")

    if not anki21:
        addWidgets20(ed, previous_lang)


# Highlighter widgets

# button icon
standardHeight = 20
standardWidth = 20
icon_path = os.path.join(addon_path, "icons", "button.png")


# Editor widgets in Anki 2.0

# This is taken from the aqt source code
def add_plugin_button_(self,
                       ed,
                       name,
                       func,
                       text="",
                       key=None,
                       tip=None,
                       height=False,
                       width=False,
                       icon=None,
                       check=False,
                       native=False,
                       canDisable=True):

    b = QPushButton(text)

    if check:
        b.clicked[bool].connect(func)
    else:
        b.clicked.connect(func)

    if height:
        b.setFixedHeight(height)
    if width:
        b.setFixedWidth(width)

    if not native:
        b.setStyle(ed.plastiqueStyle)
        b.setFocusPolicy(Qt.NoFocus)
    else:
        b.setAutoDefault(False)

    if icon:
        b.setIcon(QIcon(icon))
    if key:
        b.setShortcut(QKeySequence(key))
    if tip:
        b.setToolTip(tip)
    if check:
        b.setCheckable(True)

    self.addWidget(b)  # this part is changed

    if canDisable:
        ed._buttons[name] = b
    return b


def add_code_langs_combobox(self, func, previous_lang):
    combo = QComboBox()
    combo.addItem(previous_lang)
    
    if LIMITED_LANGS:
        selection = LIMITED_LANGS
    else:
        selection = sorted(LANGUAGES_MAP.keys(), key=string.lower)
    
    for lang in selection:
        combo.addItem(lang)

    combo.activated[str].connect(func)
    self.addWidget(combo)
    return combo


QSplitter.add_plugin_button_ = add_plugin_button_
QSplitter.add_code_langs_combobox = add_code_langs_combobox


def addWidgets20(ed, previous_lang):
    # Add the buttons to the Icon Box
    splitter = QSplitter()
    splitter.add_plugin_button_(ed,
                                "highlight_code",
                                lambda _: highlight_code(ed),
                                key=HOTKEY,
                                text="",
                                icon=icon_path,
                                tip=_("Paste highlighted code ({})".format(HOTKEY)),
                                check=False)
    splitter.add_code_langs_combobox(
        lambda lang: onCodeHighlightLangSelect(ed, lang), previous_lang)
    splitter.setFrameStyle(QFrame.Plain)
    rect = splitter.frameRect()
    splitter.setFrameRect(rect.adjusted(10, 0, -10, 0))
    ed.iconsBox.addWidget(splitter)


def onCodeHighlightLangSelect(ed, lang):
    try:
        alias = LANGUAGES_MAP[lang]
    except KeyError as e:
        print(e)
        showError(ERR_LEXER, parent=ed.parentWindow)
        ed.codeHighlightLangAlias = ""
        return False
    set_default_lang(mw, lang)
    ed.codeHighlightLangAlias = alias


# Editor widgets in Anki 2.1

select_elm = ("""<select onchange='pycmd("shLang:" +"""
              """ this.selectedOptions[0].text)' """
              """style='vertical-align: top;'>{}</select>""")


def onSetupButtons21(buttons, ed):
    """Add buttons to Editor for Anki 2.1.x"""
    # no need for a lambda since onBridgeCmd passes current editor instance
    # to method anyway (cf. "self._links[cmd](self)")
    b = ed.addButton(icon_path, "CH", highlight_code,
                         tip="Paste highlighted code ({})".format(HOTKEY),
                         keys=HOTKEY)
    buttons.append(b)

    # HTML "combobox"
    previous_lang = get_default_lang(mw)

    option_str = """<option>{}</option>"""
    options = []

    if LIMITED_LANGS:
        selection = LIMITED_LANGS
    else:
        selection = sorted(LANGUAGES_MAP.keys(), key=string.lower)

    options.append(option_str.format(previous_lang))
    for lang in selection:
        options.append(option_str.format(lang))

    combo = select_elm.format("".join(options))
    buttons.append(combo)

    return buttons


def onBridgeCmd(ed, cmd, _old):
    if not cmd.startswith("shLang"):
        return _old(ed, cmd)
    (type, lang) = cmd.split(":")
    onCodeHighlightLangSelect(ed, lang)


# Actual code highlighting


def highlight_code(ed):
    addon_conf = mw.col.conf['syntax_highlighting_conf']

    #  Do we want line numbers? linenos is either true or false according
    # to the user's preferences
    linenos = addon_conf['linenos']

    centerfragments = addon_conf['centerfragments']

    # Do we want to use css classes or have formatting directly in HTML?
    # Using css classes takes up less space and gives the user more
    # customization options, but is less self-contained as it requires
    # setting the styling on every note type where code is used
    noclasses = not addon_conf['cssclasses']

    selected_text = ed.web.selectedText()
    if selected_text:
        #  Sometimes, self.web.selectedText() contains the unicode character
        # '\u00A0' (non-breaking space). This character messes with the
        # formatter for highlighted code. To correct this, we replace all
        # '\u00A0' characters with regular space characters
        code = selected_text.replace('\u00A0', ' ')
    else:
        clipboard = QApplication.clipboard()
        # Get the code from the clipboard
        code = clipboard.text()

    langAlias = ed.codeHighlightLangAlias

    # Select the lexer for the correct language
    try:
        my_lexer = get_lexer_by_name(langAlias, stripall=True)
    except ClassNotFound as e:
        print(e)
        showError(ERR_LEXER, parent=ed.parentWindow)
        return False

    # Create html formatter object including flags for line nums and css classes
    try:
        my_formatter = HtmlFormatter(
            linenos=linenos, noclasses=noclasses,
            font_size=16, style=STYLE)
    except ClassNotFound as e:
        print(e)
        showError(ERR_STYLE, parent=ed.parentWindow)
        return False

    if linenos:
        if centerfragments:
            pretty_code = "".join(["<center>",
                                   highlight(code, my_lexer, my_formatter),
                                   "</center><br>"])
        else:
            pretty_code = "".join([highlight(code, my_lexer, my_formatter),
                                   "<br>"])
    # TODO: understand why this is neccessary
    else:
        if centerfragments:
            pretty_code = "".join(["<center>",
                                   highlight(code, my_lexer, my_formatter),
                                   "</center><br>"])
        else:
            pretty_code = "".join([highlight(code, my_lexer, my_formatter),
                                   "<br>"])

    pretty_code = process_html(pretty_code)

    # These two lines insert a piece of HTML in the current cursor position
    ed.web.eval("document.execCommand('inserthtml', false, %s);"
                % json.dumps(pretty_code))


def process_html(html):
    """Modify highlighter output to address some Anki idiosyncracies"""
    # 1.) "Escape" curly bracket sequences reserved to Anki's card template
    # system by placing an invisible html tag inbetween
    html = re.sub(r"{{", "{<!---->{", html)
    html = re.sub(r"}}", "}<!---->}", html)
    return html

# Hooks and monkey-patches

if anki21:
    addHook("setupEditorButtons", onSetupButtons21)
    Editor.onBridgeCmd = wrap(Editor.onBridgeCmd, onBridgeCmd, "around")

Editor.__init__ = wrap(Editor.__init__, init_highlighter)
