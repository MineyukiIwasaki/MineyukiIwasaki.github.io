#!/usr/bin/python3
# coding: utf-8
# (c) 2021 Mineyuki Iwasaki

import os
import re

DEPLOY_PATH = 'docs-local'
EXTENSIONS = ('.css', '.html', '.js', '.xml')
LOCAL_PATH = 'file:///Users/mine/Documents/Website/docs-local'
LOCAL_PATH_WINDOWS = 'file://C:/Users/miney/Documents/Website/docs-local'

# Find all files
for root, _, files in os.walk(DEPLOY_PATH):
    for file in files:
        base, ext = os.path.splitext(file)
        if ext == '' or ext.lower() not in EXTENSIONS:
            continue

        # Read file
        file_path = os.path.join(root, file)
        f = open(file_path, 'r', encoding='utf-8')
        original_content = f.read()
        f.close()

        # Replace URL with local path
        content = re.sub('(["(>]{1})(https://scidoggames.com.*/)([")<]{1})', r'\1\2index.html\3', original_content)
        if os.name == 'nt':
            content = re.sub('https://scidoggames.com', LOCAL_PATH_WINDOWS, content)
        else:
            content = re.sub('https://scidoggames.com', LOCAL_PATH, content)

        # Write file
        if content == original_content:
            continue
        f = open(file_path, 'w', encoding='utf-8')
        f.write(content)
        f.close()
        print(f'Replaced {file_path}')
