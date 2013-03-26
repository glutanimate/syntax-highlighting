SyntaxHighlight
===============

Addon to add syntax highlighting to Anki

Changes in this branch
======================
* Add option to turn off centering of code fragments
* Add option to store the default language per deck
* Auto-update addon config options on addon upgrade: 
    copy defaults for new options, delete options no longer used, leave everything else untouched
* Force save of collection when addon config is updated - fixes issue where config changes weren't saved 
  unless an unrelated change caused the collection state to be written to db
