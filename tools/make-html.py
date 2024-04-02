#!/usr/bin/python
# coding: utf-8
# (c) 2021 Mineyuki Iwasaki

import datetime
import os
import re
import sys

BASE_HTML_FILENAME = 'base.html'
DEPLOY_PATH = sys.argv[1]
LOCAL_DEPLOY_PATH = 'file:///Users/mine/Documents/Website/docs-local'
LOCAL_DEPLOY_PATH_WINDOWS = 'file://C:/Users/miney/Documents/Website/docs-local'
SOURCE_PATH = 'html'

# Read base html
f = open(os.path.join(SOURCE_PATH, BASE_HTML_FILENAME), 'r', encoding='utf-8')
base_html = f.read()
f.close()

# Get <head>, <header> and <footer> of base html
base_head = re.search('<head>.*?</head>', base_html, flags=re.DOTALL).group(0)
base_header = re.search('<header>.*?</header>', base_html, flags=re.DOTALL).group(0)
base_footer = re.search('<footer>.*?</footer>', base_html, flags=re.DOTALL).group(0)

# Find all html
for root, _, files in os.walk(SOURCE_PATH):
    for file in files:
        base, ext = os.path.splitext(file)
        if ext != '.html' or file == BASE_HTML_FILENAME:
            continue

        # Read html
        f = open(os.path.join(root, file), 'r', encoding='utf-8')
        html = f.read()
        f.close()

        # Get variables from html
        color = re.search('<color> *(.*?) *</color>', html).group(1)
        description = re.search('<description> *(.*?) *</description>', html).group(1)
        icon = re.search('<icon> *(.*?) *</icon>', html).group(1)
        image = re.search('<image> *(.*?) *</image>', html).group(1)
        parallax = re.search('<parallax> *(.*?) *</parallax>', html).group(1)
        title = re.search('<title> *(.*?) *</title>', html).group(1)
        url = re.search('<url> *(.*?) *</url>', html).group(1)
        preloads = []
        for match in re.finditer('<preload> *(.*?) *</preload>', html):
            preloads.append(match.group(1))
        year = str(datetime.datetime.now().year)

        # Replace html with <head>, <header> and <footer> of base html
        html = re.sub('<head>.*?</head>', base_head, html, flags=re.DOTALL)
        html = re.sub('<header>.*?</header>', base_header, html, flags=re.DOTALL)
        html = re.sub('<footer>.*?</footer>', base_footer, html, flags=re.DOTALL)

        # Replace html with variables
        html = re.sub('__COLOR__', color, html)
        html = re.sub('__DESCRIPTION__', description, html)
        html = re.sub('__ICON__', icon, html)
        html = re.sub('__IMAGE__', image, html)
        html = re.sub('__TITLE__', title, html)
        html = re.sub('__URL__', url, html)
        html = re.sub('__YEAR__', year, html)
        if parallax == 'yes':
            html = re.sub('__PARALLAX__', '', html)
        else:
            html = re.sub('__PARALLAX__', 'color-header', html)
            html = re.sub('<script.*?javascript.js.*?</script>', '', html)
        preload_tags = ''
        for preload in preloads:
            preload_tags += f'<link rel="preload" href="{preload}" as="image" fetchpriority="high">\n'
        html = re.sub('__PRELOAD__', preload_tags, html)

        # Setup for local environment
        if sys.argv[1] == 'docs-local':
            html = re.sub('"(https://scidoggames.com.*/)"', r'"\1index.html"', html)
            if os.name == 'nt':
                html = re.sub('"https://scidoggames.com', f'"{LOCAL_DEPLOY_PATH_WINDOWS}', html)
            else:
                html = re.sub('"https://scidoggames.com', f'"{LOCAL_DEPLOY_PATH}', html)

        # Make file path and dir path
        path = re.search('https://scidoggames.com/(.*)', url).group(1)
        path = os.path.join(DEPLOY_PATH, path)
        if os.name == 'nt':
            path = path.replace('/', '\\')
        if re.search('.html', path):
            dir_path = re.sub(r'([/\\]).*.html', r'\1', path)
            file_path = path
        else:
            dir_path = path
            file_path = f'{path}index.html'

        # Make directory if not exist
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # Write html
        f = open(file_path, 'w', encoding='utf-8')
        f.write(html)
        f.close()
        print(f'Generated {file_path}')
