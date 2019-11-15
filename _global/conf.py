project = "wklchris' Gitbooks 主页"
copyright = '2019, wklchris'
author = 'wklchris'

extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax',
    'sphinx_rtd_theme'
]

language = 'zh_CN'

exclude_patterns = [
    '_build', 'Thumbs.db', '.DS_Store',
    '**.ipynb_checkpoints'
]

html_theme = "sphinx_rtd_theme"
templates_path = ['_templates']

html_static_path = ['_static']
html_css_files = ['homepage_style.css']
