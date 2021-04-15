# -*- coding: utf-8 -*-
"""
    Copyright (C) 2017 by Flavio Curella - https://github.com/fcurella/jsx-lexer

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.

    Minor changes made by Colin Hughes to get it working with Anki
"""

import re

from pygments.lexer import bygroups, include, default
from pygments.lexers.javascript import JavascriptLexer
from pygments.token import Name, Operator, Punctuation, String, Text

__all__ = ['JsxLexer']

# Use same tokens as `JavascriptLexer`, but with tags and attributes support
TOKENS = JavascriptLexer.tokens
TOKENS.update(
    {
        "jsx": [
            (
                r"(<)(/?)(>)",
                bygroups(Punctuation, Punctuation, Punctuation),
            ),  # JSXFragment <>|</>
            (r"(<)([\w]+)(\.?)", bygroups(Punctuation, Name.Tag, Punctuation), "tag"),
            (
                r"(<)(/)([\w]+)(>)",
                bygroups(Punctuation, Punctuation, Name.Tag, Punctuation),
            ),
            (
                r"(<)(/)([\w]+)",
                bygroups(Punctuation, Punctuation, Name.Tag),
                "fragment",
            ),  # Same for React.Context
        ],
        "tag": [
            (r"\s+", Text),
            (r"([\w]+\s*)(=)(\s*)", bygroups(Name.Attribute, Operator, Text), "attr"),
            (r"[{}]+", Punctuation),
            (r"[\w\.]+", Name.Attribute),
            (r"(/?)(\s*)(>)", bygroups(Punctuation, Text, Punctuation), "#pop"),
        ],
        "fragment": [
            (r"(.)([\w]+)", bygroups(Punctuation, Name.Attribute)),
            (r"(>)", bygroups(Punctuation), "#pop"),
        ],
        "attr": [
            ("{", Punctuation, "expression"),
            ('".*?"', String, "#pop"),
            ("'.*?'", String, "#pop"),
            default("#pop"),
        ],
        "expression": [
            ("{", Punctuation, "#push"),
            ("}", Punctuation, "#pop"),
            include("root"),
        ],
    }
)
TOKENS["root"].insert(0, include("jsx"))


class JsxLexer(JavascriptLexer):
    name = "JSX"
    aliases = ["jsx", "react"]
    filenames = ["*.jsx", "*.react"]
    mimetypes = ["text/jsx", "text/typescript-jsx"]

    flags = re.MULTILINE | re.DOTALL | re.UNICODE

    tokens = TOKENS