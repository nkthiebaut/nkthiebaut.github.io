#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = "Nicolas Thiebaut"
SITENAME = "Data4thought: data science blog"
SITEURL = "https://nkthiebaut.github.io"
SITETITLE = "Data4thought"
SITESUBTITLE = "Nicolas Thiebaut's data science blog"
SITEDESCRIPTION = "Nicolas Thiebaut's data science blog"
SITELOGO = SITEURL + "/images/PhotoThiebaut.jpg"
FAVICON = SITEURL + "/images/favicon.ico"

PATH = "content"
MAIN_MENU = True
STATIC_PATHS = ["images", "pdfs"]

TIMEZONE = "Europe/Paris"
THEME = os.path.join(os.getcwd(), "themes", "neat")

DEFAULT_LANG = "en"
# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (
    ("linkedin", "https://www.linkedin.com/in/nthiebaut"),
    ("github", "https://github.com/nkthiebaut/"),
    ("twitter", "https://twitter.com/NicoThiebaut"),
)

# MENUITEMS = (('Archives', '/archives.html'),
#             ('Categories', '/categories.html'),
#             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
MARKUP = ("md", "ipynb")

from pelican_jupyter import markup as nb_markup
from pelican_jupyter import liquid as nb_liquid # import pelican-jupyter
from pelican.plugins import liquid_tags
from pelican.plugins import render_math

PLUGINS = [liquid_tags, nb_markup, 'liquid_tags.img', nb_liquid, 'representative_image', "render_math"]

LIQUID_TAGS = ["img", "include_code", "gram", "video", "youtube", "notebook"]
LIQUID_CONFIGS = (("IPYNB_FIX_CSS", "False", ""), 
                  ("IPYNB_SKIP_CSS", "False", ""), 
                  ("IPYNB_EXPORT_TEMPLATE", "base", ""),)
MATH_JAX = {'tex_extensions': ['color.js']}

IPYNB_FIX_CSS = True
IPYNB_SKIP_CSS = False
# IPYNB_EXPORT_TEMPLATE = "./export.tpl"


PLUGIN_PATHS = ["./plugins"]
PLUGINS = ["share_post.share_post"]
IGNORE_FILES = [".ipynb_checkpoints"]

# PLUGIN_PATHS = ['./plugins']
# PLUGINS = ['ipynb.markup', 'share_post.share_post']
