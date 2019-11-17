project = '时间序列浅谈'
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
templates_path = ['../../_global/_templates']

html_static_path = ['../../_global/_static']
html_css_files = ['style.css']

# Config: nbsphinx
mathjax_config = {
    'TeX': {'equationNumbers': {'autoNumber': 'AMS', 'useLabelIds': True}}
}
