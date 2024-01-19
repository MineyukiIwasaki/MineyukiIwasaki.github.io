#!/usr/bin/python
# coding: utf-8
# (c) 2021 Mineyuki Iwasaki

import os
import re

BASE_HTML_FILENAME = 'base.html'
DEPLOY_PATH = 'docs'
SITEMAP_FILENAME = 'sitemap.xml'
SOURCE_PATH = 'html'

# Open sitemap
f = open(DEPLOY_PATH + '/' + SITEMAP_FILENAME, 'w', encoding='utf-8')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

# Find all html
for dirpath, dirnames, filenames in os.walk(SOURCE_PATH):
    for filename in sorted(filenames):
        base, ext = os.path.splitext(filename)
        if ext != '.html' or filename == BASE_HTML_FILENAME:
            continue

        # Read html
        h = open(dirpath + '/' + filename, 'r', encoding='utf-8')
        html = h.read()
        h.close()

        # Get url from html
        url = re.search(r'<url>\s*(.*?)\s*</url>', html, flags=re.DOTALL).group(1)

        # Write url to sitemap
        f.write('    <url>\n')
        f.write('        <loc>' + url + '</loc>\n')
        f.write('    </url>\n')

# Close sitemap
f.write('</urlset>\n')
f.close()
print(os.path.basename(__file__) + ': Generated ' + DEPLOY_PATH + '/' + SITEMAP_FILENAME + '.')
