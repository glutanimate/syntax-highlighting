# -*- coding: utf-8 -*-

"""
This file is part of the Syntax Highlighting add-on for Anki.

Configuration shim between Anki 2.0 and Anki 2.1

Copyright: (c) 2018 Glutanimate <https://glutanimate.com/>
License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>
"""

import os
import io

from aqt import mw
from anki.utils import json
from anki.hooks import addHook

from .consts import *

defaults_path = os.path.join(addon_path, "config.json")
meta_path = os.path.join(addon_path, "meta.json")

###############################################################
###
# Configurable preferences
###
###############################################################

# Defaults conf
# - we create a new item in the collection's configuration. This syncs the
# options across machines (but not on mobile)
default_conf = {'linenos': True,  # show numbers by default
                'centerfragments': True,  # Use <center> when generating code fragments
                'cssclasses': False,  # Use css classes instead of colors directly in html
                'defaultlangperdeck': True,  # Default to last used language per deck
                'deckdefaultlang': {},  # Map to store the default language per deck
                'lang': 'Python'}  # default language is Python

###############################################################


# Synced conf

def sync_keys(tosync, ref):
    for key in [x for x in list(tosync.keys()) if x not in ref]:
        del(tosync[key])

    for key in [x for x in list(ref.keys()) if x not in tosync]:
        tosync[key] = ref[key]


def sync_config_with_default(col):
    if not 'syntax_highlighting_conf' in col.conf:
        col.set_config('syntax_highlighting_conf', default_conf)
    else:
        sync_keys(col.get_config('syntax_highlighting_conf'), default_conf)

    # Mark collection state as modified, else config changes get lost unless
    # some unrelated action triggers the flush of collection data to db
    col.setMod()
    # col.flush()

def setupSyncedConf():
    # If config options have changed, sync with default config first
    sync_config_with_default(mw.col)

addHook("profileLoaded", setupSyncedConf)

# Local conf

def getConfig():
    return mw.addonManager.getConfig(__name__)

def writeConfig(config):
    mw.addonManager.writeConfig(__name__, config)
local_conf = getConfig()
