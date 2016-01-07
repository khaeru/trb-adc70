#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)

import plugins.trb
import private as private_settings

AUTHOR = 'TRB/ADC70'
SITENAME = 'Transportation Energy Committee'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = 'themes/pelican-bootstrap3'
# DISPLAY_PAGES_ON_MENU = T

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# ADC70 settings

PLUGINS = [plugins.trb]
TRB = private_settings.TRB
# STATIC_PATHS = ['pdf']