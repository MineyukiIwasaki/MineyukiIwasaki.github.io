#!/usr/bin/python
# coding: utf-8
# (c) 2021 Mineyuki Iwasaki

import os
import re
import sys

DEPLOY_PATH = sys.argv[1]

# Find all html, css, js and svg
for root, _, files in os.walk(DEPLOY_PATH):
    for file in files:
        base, ext = os.path.splitext(file)
        if ext != '.html' and ext != '.css' and ext != '.js' and ext != '.svg':
            continue

        # Read html, css, js and svg
        file_path = os.path.join(root, file)
        f = open(file_path, 'r', encoding='utf-8')
        original_content = f.read()
        f.close()

        # Optimize html
        if ext == '.html':
            # Remove comments
            content = re.sub('<!--.*?-->', '', original_content, flags=re.DOTALL)
            # Remove spaces
            content = re.sub('\n', ' ', content)
            content = re.sub(' +', ' ', content)
            content = re.sub(' <', '<', content)
            content = re.sub('> ', '>', content)
            content = re.sub('>', '>\n', content)
            content = re.sub('>\n(.+?)<', r'>\1<', content)
            content = re.sub('\n$', '', content)
            # Remove empty tags
            content = re.sub('<h[1-6]{1}>\n</h[1-6]{1}>\n', '', content)
            content = re.sub('<div>\n</div>\n', '', content)
            # Force inline
            content = re.sub('\n</i>', '</i>', content)
            content = re.sub('\n</iframe>', '</iframe>', content)
            content = re.sub('\n</script>', '</script>', content)
            content = re.sub('(<h[1-6]{1}>)\n', r'\1', content)
            content = re.sub('\n(</h[1-6]{1}>)', r'\1', content)
            content = re.sub('<li>\n', '<li>', content)
            content = re.sub('\n</li>', '</li>', content)
            # Specific cases
            content = re.sub('<p>(.+?)<a href(.*?)</a>(.+?)</p>', r'<p>\1 <a href\2</a> \3</p>', content)
            match = re.search('<meta name="viewport" content=".*?">', content).group(0).replace(', ', ',')
            content = re.sub('<meta name="viewport" content=".*?">', match, content)
            match = re.search('<script>.*?</script>', content).group(0).replace(' ', '').replace('function', 'function ').replace('new', 'new ')
            content = re.sub('<script>.*?</script>', match, content)

        # Optimize css
        if ext == '.css':
            # Remove comments
            content = re.sub(r'/\*.*?\*/', '', original_content, flags=re.DOTALL)
            # Remove spaces
            content = re.sub('\n', ' ', content)
            content = re.sub(' +', ' ', content)
            content = re.sub(r' *\( *', '(', content)
            content = re.sub(r' *\) *', ')', content)
            content = re.sub(r' *\* *', '*', content)
            content = re.sub(' *, *', ',', content)
            content = re.sub(r' *\/ *', '/', content)
            content = re.sub(' *: *', ':', content)
            content = re.sub(' *; *', ';', content)
            content = re.sub(' *@ *', '@', content)
            content = re.sub(' *{ *', '{', content)
            content = re.sub(' *} *', '}', content)
            content = re.sub('}', '}\n', content)
            content = re.sub('^ +', '', content)
            content = re.sub('\n$', '', content)
            # Specific cases
            content = re.sub('@(.*?){(.*?){(.*?)}\n}\n', r'@\1{\2{\3}}\n', content)
            content = re.sub('@(.*?){(.*?){(.*?)}\n(.*?){(.*?)}\n}\n', r'@\1{\2{\3}\4{\5}}\n', content)

        # Optimize js
        if ext == '.js':
            # Remove comments
            content = re.sub(r'/\*.*?\*/', '', original_content, flags=re.DOTALL)
            content = re.sub('//.*?\n', '', content)
            # Remove spaces
            content = re.sub('\n', ' ', content)
            content = re.sub(' +', ' ', content)
            content = re.sub(' *& *', '&', content)
            content = re.sub(r' *\( *', '(', content)
            content = re.sub(r' *\) *', ')', content)
            content = re.sub(r' *\* *', '*', content)
            content = re.sub(r' *\+ *', '+', content)
            content = re.sub(' *, *', ',', content)
            content = re.sub(' *- *', '-', content)
            content = re.sub(r' *\/ *', '/', content)
            content = re.sub(' *; *', ';', content)
            content = re.sub(' *< *', '<', content)
            content = re.sub(' *= *', '=', content)
            content = re.sub(' *> *', '>', content)
            content = re.sub(' *{ *', '{', content)
            content = re.sub(r' *\| *', '|', content)
            content = re.sub(' *} *', '}', content)
            content = re.sub('else', '\nelse', content)
            content = re.sub('if', '\nif', content)
            content = re.sub('let', '\nlet', content)
            content = re.sub('^ +', '', content)
            content = re.sub('\n$', '', content)

        # Optimize svg
        if ext == '.svg':
            # Remove spaces
            content = re.sub('\n', ' ', original_content)
            content = re.sub(' +', ' ', content)
            content = re.sub(' <', '<', content)
            content = re.sub('> ', '>', content)
            content = re.sub(' />', '/>', content)
            content = re.sub('>', '>\n', content)
            content = re.sub('\n$', '', content)
            # Remove unused tags
            content = re.sub(r'<\?xml.*?\?>\n', '', content)
            content = re.sub('<defs.*?/>\n', '', content)
            content = re.sub('<metadata.*?</metadata>\n', '', content, flags=re.DOTALL)
            content = re.sub('<sodipodi:namedview.*?</sodipodi:namedview>\n', '', content, flags=re.DOTALL)
            content = re.sub('<title>.*?</title>\n', '', content, flags=re.DOTALL)
            # Remove unused attributes
            content = re.sub(' *data-name=".*?"', '', content)
            content = re.sub(' *id=".*?"', '', content)
            content = re.sub(' *inkscape:connector-curvature=".*?"', '', content)
            content = re.sub(' *inkscape:export-filename=".*?"', '', content)
            content = re.sub(' *inkscape:export-xdpi=".*?"', '', content)
            content = re.sub(' *inkscape:export-ydpi=".*?"', '', content)
            content = re.sub(' *inkscape:groupmode=".*?"', '', content)
            content = re.sub(' *inkscape:label=".*?"', '', content)
            content = re.sub(' *inkscape:version=".*?"', '', content)
            content = re.sub(' *sodipodi:docname=".*?"', '', content)
            content = re.sub(' *sodipodi:nodetypes=".*?"', '', content)
            content = re.sub(' *version=".*?"', '', content)
            content = re.sub(' *xmlns:cc=".*?"', '', content)
            content = re.sub(' *xmlns:dc=".*?"', '', content)
            content = re.sub(' *xmlns:inkscape=".*?"', '', content)
            content = re.sub(' *xmlns:rdf=".*?"', '', content)
            content = re.sub(' *xmlns:sodipodi=".*?"', '', content)
            content = re.sub(' *xmlns:svg=".*?"', '', content)

        # Write html, css, js and svg
        f = open(file_path, 'w', encoding='utf-8')
        f.write(content)
        f.close()
        print(f'Optimized {file_path} {len(original_content) / 1000:.2f}kb -> {len(content) / 1000:.2f}kb' + \
            f' ({100 * len(content) / len(original_content):.2f}%)')
