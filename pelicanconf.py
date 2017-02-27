#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
from datetime import datetime

AUTHOR = u'FSFW Dresden'
SITENAME = u'FSFW Dresden'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'de'
LOCALE = 'de_DE.UTF-8'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
# (this is overridden by the publishconf.py used for publishing)
RELATIVE_URLS = True

THEME = './themes/fsfw-dresden'

STATIC_PATHS = ["img"]

PLUGIN_PATHS = ['pelican-plugins', '.']
PLUGINS = ['filetime_from_git', 'open_graph', 'neighbors']

INDEX_SAVE_AS = 'blog.html'

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'

YEAR_START = 2017
YEAR_END = datetime.utcnow().year


BUILD_TIME = datetime.utcnow()
IS_STAGING = bool(os.environ.get("STAGING", ""))
COMMIT_ID = os.environ.get("COMMIT", "")[:7]
