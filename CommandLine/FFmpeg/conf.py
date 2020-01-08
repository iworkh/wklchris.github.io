project = 'FFmpeg简明用例指南'
copyright = '2020, wklchris'
author = 'wklchris'

extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax'
]

language = 'zh_cn'

exclude_patterns = [
    '_build', 'Thumbs.db', '.DS_Store',
    '**.ipynb_checkpoints'
]

html_theme = "sphinx_rtd_theme"
templates_path = ['../../_global/_templates']

html_static_path = ['../../_global/_static']
html_css_files = ['style.css']
