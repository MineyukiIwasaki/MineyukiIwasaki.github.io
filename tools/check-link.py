#!/usr/bin/python
# coding: utf-8
# (c) 2021 Mineyuki Iwasaki

import os
import re
import requests
import sys

EXTENSIONS = ('.css', '.html', '.js', '.svg', '.xml')
PRECONNECTS = ('https://fonts.gstatic.com', 'https://use.fontawesome.com')
DEPLOY_PATH = sys.argv[1]

# Find all URLs
urls = []
for root, _, files in os.walk(DEPLOY_PATH):
    for file in files:
        base, ext = os.path.splitext(file)
        if ext.lower() not in EXTENSIONS:
            continue
        f = open(os.path.join(root, file), 'r', encoding='utf-8')
        html = f.read()
        f.close()
        for match in re.finditer(r'[>\(\'"]{1}(http.*?)[<\)\'"]{1}', html):
            urls.append(match.group(1))
urls = list(dict.fromkeys(urls))
urls.sort()

# Make sitemap
for url in urls:
    if url in PRECONNECTS:
        continue
    try:
        response = requests.head(url, allow_redirects=True)
        response.raise_for_status()
        print(f'OK {url}')
    except requests.exceptions.RequestException:
        print(f'NG {url}')
