#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'wklchris'
SITENAME = "Wklchris' Website"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Tijuana'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Links
LINKS = (('About', '/pages/about.html'),)
SOCIAL = (('Github', 'https://github.com/wklchris'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#
# ----- Customization -----
#
#   SOCIAL and DEFAULT_LANG are changed above.
#   Other changes are listed below.

DEFAULT_CATEGORY = 'misc'
SLUGIFY_SOURCE = 'basename'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'zh_cn': '%Y-%m-%d(%a)',
}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites']

# Customized theme, modified for multi-lang support
THEME = 'themes/notmyidea/'

# 
# Plugin <i18n_subsites>: Website in Multi-languages
#
I18N_SUBSITES = {
    'zh_cn': {
        'SITENAME': "Wklchris 个人站",
        'TIMEZONE': 'Asia/Shanghai',
        'LINKS': (('关于我', '/pages/about-zh_cn.html'),)
        }
    }
## Show text on language buttons
languages_lookup = {
             'en': 'English',
             'zh_cn': '简体中文',
             }

def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]

JINJA_FILTERS = {'lookup_lang_name': lookup_lang_name}
