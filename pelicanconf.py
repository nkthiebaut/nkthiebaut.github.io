#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Nicolas Thiebaut'
SITENAME = "Data4thought: data science blog"
SITEURL = 'https://nkthiebaut.github.io'
SITETITLE = "Data4thought"
SITESUBTITLE = "Nicolas Thiebaut's data science blog"
SITEDESCRIPTION = "Nicolas Thiebaut's data science blog"
SITELOGO = SITEURL + '/images/PhotoThiebaut.jpg'
FAVICON = SITEURL + '/images/favicon.ico'

PATH = 'content'
MAIN_MENU = True
STATIC_PATHS = ['images', 'pdfs']

TIMEZONE = 'Europe/Paris'
THEME = os.path.join(os.getcwd(), "themes", "Flex")

DEFAULT_LANG = 'en'
# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/nthiebaut'),
          ('github', 'https://github.com/nkthiebaut/'),
          ('twitter', 'https://twitter.com/NicoThiebaut'),)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup', 'share_post.share_post']
