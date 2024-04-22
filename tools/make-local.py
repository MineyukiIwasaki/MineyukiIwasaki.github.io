#!/usr/bin/python
# coding: utf-8
# (c) 2021 Mineyuki Iwasaki

import datetime
import os
import re
import sys

DEPLOY_PATH = 'docs-local'
LOCAL_DEPLOY_PATH = 'file:///Users/mine/Documents/Website/docs-local'
LOCAL_DEPLOY_PATH_WINDOWS = 'file://C:/Users/miney/Documents/Website/docs-local'

# Find all html
for root, _, files in os.walk(DEPLOY_PATH):
    for file in files:
        base, ext = os.path.splitext(file)
        if ext != '.html' and ext != '.css' and ext != '.xml':
            continue

        # Read html
        f = open(os.path.join(root, file), 'r', encoding='utf-8')
        original_content = f.read()
        f.close()

        # Setup for local environment
        content = original_content
        #content = re.sub('"(https://scidoggames.com.*/)"', r'"\1index.html"', content)
        content = re.sub('(["(>]{1})(https://scidoggames.com.*/)([")<]{1})', r'\1\2index.html\3', content)
        if os.name == 'nt':
            content = re.sub('https://scidoggames.com', LOCAL_DEPLOY_PATH_WINDOWS, content)
        else:
            content = re.sub('https://scidoggames.com', LOCAL_DEPLOY_PATH, content)

        # Write html
        f = open(os.path.join(root, file), 'w', encoding='utf-8')
        f.write(content)
        f.close()
        print(f'Replaced {os.path.join(root, file)}')
