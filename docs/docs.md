NEW:
- added option to use css classes (disabled by default)
- you can now toggle line numbers on or off in the source code
- some small changes have been made. Everyone should upgrade

Highlight Code
---------------------
This addon allows you to copy source code from a number of programming (and markup) languages and paste it in an Anki field with proper syntax highlighting.
The highlighted code is stored by Anki in HTML with CSS, in a copy/paste friendly format, which is useful if you want to correct a mistake in your code.

How to use it
------------------- 
The addon adds a lightning bolt icon and a drop down menu to the icons bar of the note editor.
To paste some highlighted code, you first copy the correct code to the System Clipboard (with Ctrl+C under Windows, for example).
You can write the code directly in Anki and copy form there, but I find it much easier to write it on a proper text editor.
You can of course copy code from wherever you want, including a webpage.
Please note that is you want to highlight code from outside of Anki, just selecting the code is not enough.
You really have to copy it to the System Clipboard.
Now that you have copied some code, can use the dropdown menu to choose the appropriate programming language.
After that, place the cursor in the position where you want to insert the code, and click the lightning bold icon.
This will insert a HTML table with the properly highlighted code. Instead of clicking the icon to paste the code, you can use the keyboard shortcut Alt+s.
The addon remembers the last programming language you chose, even after you restart Anki. 

If you want to highlight code from Anki, you don’t need to copy it to the system clipboard.
You can just select the code and highlight it directly (by clicking the lightning bolt button or using the Alt+s shortcut)

Configuration
-----------------

You can choose whether or not to display line numbers in the highlighted source code.
Just go to Tools > Syntax Highlighting (options).
A new window will appear.
Toggle the check box on or off to display or hide the line numbers.

You can also choose whether to include the styling directly in the text html (default) or to use css classes.
Using css classes allows you more customization, and results in a smaller database size, but you'll need to manually include a styling sheet in every note type, so it's only recommended for advanced users. Here is some default css code to include in your templates:

```css
.highlight {
  text-align:left;
  font-family: droid sans mono;
  background-color: #f2f2f2;
  padding-left: 5px;
  padding-right: 5px;
}

.night_mode .highlight {
  /* Invert all of the colors when using night mode in AnkiDroid */
  color:black;
  background-color: #C2C2C2;
  filter: invert(1); -webkit-filter:invert(1);
}

.highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #808080 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0040D0 } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
```


Pygments 
-------------
All syntax highlighting is handled by the python package Pygments.
Credit for everything related to the syntax highlighting goes to the respective authors.
This addon uses a slightly customized version of the Pygments package to eliminate external dependencies. 

Author Contact: tmbb@campus.ul.pt
