Title: 本站的 Pelican 构建
Date: 2019-01
Lang: zh_cn
Category: Blog

# Pelican 构建站点

## 主题

如果不满意站点主题，可以前往 [Pelican 主题站](http://www.pelicanthemes.com/) 自行选择．本站使用的主题是默认的 notmyidea 主题（有改动），要配置这个默认主题，用户可以前往 Python 安装目录下的如下路径复制：

```
\Lib\site-packages\pelican\themes
```

然后回到站点文件夹，打开 `pelicanconf.py` 配置文件：

```python
THEME = 'themes/notmyidea/'
```

接着就可以对主题文件夹下的 static 与 templates 子文件夹中的内容进行修改了．

## 双语或多语站点

借助 [i18n_subsites](https://github.com/smartass101/pelican-plugins/tree/master/i18n_subsites) 插件，我们可以较轻松地配置双语站点．在 `pelicanconf.py` 配置文件中添加：

```python
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites']
```

下面介绍本站使用的方法．先将 notmyidea 主题配置完毕．

然后到主题文件夹中，在 `base.html` 的 `<nav><ul>` 后一行添加：

```html
    {% if lang_siteurls %}
    {% for lang, siteurl in lang_siteurls.items() %}
    <li{% if lang == DEFAULT_LANG %} class="active"{% endif %}>
            <a href="{{ siteurl }}/">{{ lang | lookup_lang_name }}</a>
    </li>
    {% endfor %}
    <li style="background-color: white; padding: 5px;">&nbsp</li>
    {% endif %}
```

与上述代码配套的是 `pelicanconf.py` 中对插件的如下配置：

```python
# Overriding parameters
I18N_SUBSITES = {
    'zh_cn': {
        'SITENAME': "Wklchris 个人站",
        ... # Other keys
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
```

最后，记住对所有的文章都添加 `lang` 标签．

## 重定向

有时需要将多个链接定向到同一篇文章上，这时可以使用插件 [pelican-alias](https://github.com/Nitron/pelican-alias)．

本站利用该插件，将作者信息页定向到了 About 页面．
