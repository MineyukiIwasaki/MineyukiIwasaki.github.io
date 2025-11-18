#!/usr/bin/python3
# coding: utf-8
# (c) 2021 Mineyuki Iwasaki

import os
import re

DEPLOY_PATH = 'docs'
SITEMAP_PATH = os.path.join(DEPLOY_PATH, 'sitemap.xml')

# Find all URLs
urls = []
for root, _, files in os.walk(DEPLOY_PATH):
    for file in files:
        base, ext = os.path.splitext(file)
        if ext != '.html':
            continue
        f = open(os.path.join(root, file), 'r', encoding='utf-8')
        html = f.read()
        f.close()
        urls.append(re.search('<link rel="canonical" href="(.*?)">', html).group(1))
urls.sort()

# Make sitemap
f = open(SITEMAP_PATH, 'w', encoding='utf-8')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
for url in urls:
    f.write(f'<url><loc>{url}</loc></url>\n')
f.write('</urlset>')
f.close()
print(f'Generated {SITEMAP_PATH}')
