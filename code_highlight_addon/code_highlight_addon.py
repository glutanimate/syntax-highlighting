# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import os
import sys

from aqt import editor, addons, mw
#from aqt.utils import showInfo
  # For those who are wondering, 'mw' means "Main Window"
from anki.utils import json
from anki import hooks

# import the lightning bolt icon
from resources import *

def debug_trace():
  '''Set a tracepoint in the Python debugger that works with Qt'''
  from PyQt4.QtCore import pyqtRemoveInputHook
  from pdb import set_trace
  pyqtRemoveInputHook()
  set_trace()

###############################################################
###
### Utilities to generate buttons
###
###############################################################
standardHeight = 20
standardWidth  = 20

# This is taken from the aqt source code to 
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
        b.connect(b, SIGNAL("clicked(bool)"), func)
    else:
        b.connect(b, SIGNAL("clicked()"), func)
        
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
        
    self.addWidget(b) # this part is changed
        
    if canDisable:
        ed._buttons[name] = b
    return b

###############################################################
def add_code_langs_combobox(self, func, previous_lang):
    combo = QComboBox()
    combo.addItem(previous_lang)
    for lang in sorted(LANGUAGES_MAP.iterkeys()):
        combo.addItem(lang)
        
    combo.activated[str].connect(func)
    self.addWidget(combo)
    return combo

###############################################################
###
### Configurable preferences
###
###############################################################
#### Defaults conf
####  - we create a new item in mw.col.conf. This syncs the
####    options across machines (but not on mobile)
default_conf = {'linenos': True,  # show numbers by default
                'centerfragments': True, # Use <center> when generating code fragments
                'cssclasses': False, # Use css classes instead of colors directly in html
                'defaultlangperdeck': True, # Default to last used language per deck
                'deckdefaultlang': {}, # Map to store the default language per deck
                'lang': 'Python'} # default language is Python 
###############################################################

def sync_keys(tosync, ref):
    for key in [ x for x in tosync.keys() if x not in ref ]:
        del(tosync[key])

    for key in [ x for x in ref.keys() if x not in tosync ]:
        tosync[key] = ref[key]

def sync_config_with_default(col):
    if not 'syntax_highlighting_conf' in col.conf:
        col.conf['syntax_highlighting_conf'] = default_conf
    else:
        sync_keys(col.conf['syntax_highlighting_conf'], default_conf)

    # Mark collection state as modified, else config changes get lost unless 
    # some unrelated action triggers the flush of collection data to db
    col.setMod()
    #col.flush()

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
    addon_conf['lang'] = lang # Always update the overall default
    if addon_conf['defaultlangperdeck']:
        deck_name = get_deck_name(mw)
        if deck_name:
            addon_conf['deckdefaultlang'][deck_name] = lang

class SyntaxHighlighting_Options(QWidget):
    def __init__(self, mw):
        super(SyntaxHighlighting_Options, self).__init__()
        self.mw = mw
        self.addon_conf = None
    
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
        # If config options have changed, sync with default config first
        sync_config_with_default(self.mw.col)

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

        defaultlangperdeck_label = QLabel('<b>Default to last language used per deck</b>')
        defaultlangperdeck_checkbox = QCheckBox('')
        defaultlangperdeck_checkbox.setChecked(self.addon_conf['defaultlangperdeck'])
        defaultlangperdeck_checkbox.stateChanged.connect(self.switch_defaultlangperdeck)


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
        self.show()


mw.SyntaxHighlighting_Options = SyntaxHighlighting_Options(mw)

options_action = QAction("Syntax Highlighting Options ...", mw)
mw.connect(options_action,
           SIGNAL("triggered()"),
           mw.SyntaxHighlighting_Options.setupUi)
mw.form.menuTools.addAction(options_action)
###############################################################

###############################################################
QSplitter.add_plugin_button_ = add_plugin_button_
QSplitter.add_code_langs_combobox = add_code_langs_combobox

def init_highlighter(ed, *args, **kwargs):
    # If config options have changed, sync with default config first
    sync_config_with_default(mw.col)

    #  Get the last selected language (or the default language if the user
    # has never chosen any)
    previous_lang = get_default_lang(mw)
    ed.codeHighlightLangAlias = LANGUAGES_MAP[previous_lang]

    ### Add the buttons to the Icon Box
    splitter = QSplitter()
    splitter.add_plugin_button_(ed,
                             "highlight_code",
                             ed.highlight_code,
                             key="Alt+s",
                             height=standardHeight,
                             width=standardWidth,
                             text="",
                             icon=":/icons/button-icon.png",
                             tip=_("Paste highlighted code (Alt+s)"),
                             check=False)
    splitter.add_code_langs_combobox(ed.onCodeHighlightLangSelect, previous_lang)
    splitter.setFrameStyle(QFrame.Plain)
    rect = splitter.frameRect()
    splitter.setFrameRect(rect.adjusted(10,0,-10,0))
    ed.iconsBox.addWidget(splitter)

def onCodeHighlightLangSelect(self, lang):
    set_default_lang(mw, lang)
    alias = LANGUAGES_MAP[lang]
    self.codeHighlightLangAlias = alias

###############################################################

###############################################################
###
### Deals with highlighting
###
###############################################################
def addons_folder(): return mw.pm.addonFolder()

#  Tell Python where to look here for our stripped down
# version of the Pygments package: 
try:
    __import__('pygments')
except ImportError:
    sys.path.insert(0, os.path.join(addons_folder(), "code_highlight_addon"))

# Choose default language from the last to be used
#lang_file_path = os.path.join(addons_folder(), "code_highlight_addon", "lang.txt")
                                   
from pygments import highlight
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.formatters import HtmlFormatter

# This code sets a correspondence between:
#  The "language names": long, descriptive names we want
#   to show the user AND
#  The "language aliases": short, cryptic names for internal
#   use by HtmlFormatter 
LANGUAGES_MAP = {}
for lex in get_all_lexers():
    #  This line uses the somewhat weird structure of the the map
    # returned by get_all_lexers
    LANGUAGES_MAP[lex[0]] = lex[1][0]
    
###############################################################
def highlight_code(self):
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

    selected_text = self.web.selectedText()
    if selected_text:
        #  Sometimes, self.web.selectedText() contains the unicode character
        # '\u00A0' (non-breaking space). This character messes with the
        # formatter for highlighted code. To correct this, we replace all
        # '\u00A0' characters with regular space characters
        code = selected_text.replace(u'\u00A0', ' ')
    else:
        clipboard = QApplication.clipboard()
        # Get the code from the clipboard
        code = clipboard.text()
    
    langAlias = self.codeHighlightLangAlias
    
    # Select the lexer for the correct language
    my_lexer = get_lexer_by_name(langAlias, stripall=True)
    
    # Create html formatter object including flags for line nums and css classes
    my_formatter = HtmlFormatter(linenos=linenos, noclasses=noclasses, font_size=16)
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
            pretty_code = "".join(["<center><table><tbody><tr><td>",
                                   highlight(code, my_lexer, my_formatter),
                                   "</td></tr></tbody></table></center><br>"])
        else:
            pretty_code = "".join(["<table><tbody><tr><td>",
                                   highlight(code, my_lexer, my_formatter),
                                   "</td></tr></tbody></table><br>"])

    # These two lines insert a piece of HTML in the current cursor position
    self.web.eval("document.execCommand('inserthtml', false, %s);"
                  % json.dumps(pretty_code))

editor.Editor.onCodeHighlightLangSelect = onCodeHighlightLangSelect
editor.Editor.highlight_code = highlight_code
editor.Editor.__init__ = hooks.wrap(editor.Editor.__init__, init_highlighter)

