#!/usr/bin/python3
# coding: utf-8
#------------------------------------------------------------------------------
# (c) 2021 Mineyuki Iwasaki
#------------------------------------------------------------------------------

import datetime
import os
import re
import sys

BASE_HTML_FILENAME = 'base.html'
DEPLOY_PATH = 'docs'
LOCAL_DEPLOY_PATH = 'file:///Users/mine/Documents/github.io/docs'
LOCAL_DEPLOY_PATH_WINDOWS = 'file://C:/Users/mine/Documents/github.io/docs'
SOURCE_PATH = 'html'

# Read base html
f = open(SOURCE_PATH + '/' + BASE_HTML_FILENAME, 'r', encoding='utf-8')
base_html = f.read()
f.close()

# Get <head>, <header> and <footer> of base html
base_head = re.search('<head>.*?<\/head>', base_html, flags=re.DOTALL).group(0)
base_header = re.search('<header>.*?<\/header>', base_html, flags=re.DOTALL).group(0)
base_footer = re.search('<footer>.*?<\/footer>', base_html, flags=re.DOTALL).group(0)

# Find all html
for dirpath, dirnames, filenames in os.walk(SOURCE_PATH):
    for filename in filenames:
        base, ext = os.path.splitext(filename)
        if ext != '.html' or filename == BASE_HTML_FILENAME:
            continue

        # Read html
        f = open(dirpath + '/' + filename, 'r', encoding='utf-8')
        html = f.read()
        f.close()

        # Get variables from html
        color = re.search('(<color>)(\s*)(.*?)(\s*)(<\/color>)', html, flags=re.DOTALL).group(3)
        description = re.search('(<description>)(\s*)(.*?)(\s*)(<\/description>)', html, flags=re.DOTALL).group(3)
        icon = re.search('(<icon>)(\s*)(.*?)(\s*)(<\/icon>)', html, flags=re.DOTALL).group(3)
        image = re.search('(<image>)(\s*)(.*?)(\s*)(<\/image>)', html, flags=re.DOTALL).group(3)
        parallax = re.search('(<parallax>)(\s*)(.*?)(\s*)(<\/parallax>)', html, flags=re.DOTALL).group(3)
        title = re.search('(<title>)(\s*)(.*?)(\s*)(<\/title>)', html, flags=re.DOTALL).group(3)
        url = re.search('(<url>)(\s*)(.*?)(\s*)(<\/url>)', html, flags=re.DOTALL).group(3)
        year = str(datetime.datetime.now().year)

        # Replace html with <head>, <header> and <footer> of base html
        html = re.sub(r'<head>.*?<\/head>', base_head, html, flags=re.DOTALL)
        html = re.sub(r'<header>.*?<\/header>', base_header, html, flags=re.DOTALL)
        html = re.sub(r'<footer>.*?<\/footer>', base_footer, html, flags=re.DOTALL)

        # Replace html with variables
        html = re.sub(r'__COLOR__', color, html)
        html = re.sub(r'__DESCRIPTION__', description, html)
        html = re.sub(r'__ICON__', icon, html)
        html = re.sub(r'__IMAGE__', image, html)
        html = re.sub(r'__TITLE__', title, html)
        html = re.sub(r'__URL__', url, html)
        html = re.sub(r'__YEAR__', year, html)
        if parallax == 'yes':
            html = re.sub(r'__PARALLAX__', '', html)
        else:
            html = re.sub(r'__PARALLAX__', 'color-header', html)
            html = re.sub(r'<script.*?javascript\.js.*?<\/script>', '', html, flags=re.DOTALL)

        # Setup for local environment if argv has 'local'
        if len(sys.argv) == 2 and sys.argv[1] == 'local':
            html = re.sub(r'(https:\/\/scidoggames\.com.*?\/)\"', r'\1index.html"', html)
            if os.name == 'nt':
                html = re.sub(r'https:\/\/scidoggames\.com', LOCAL_DEPLOY_PATH_WINDOWS, html)
            else:
                html = re.sub(r'https:\/\/scidoggames\.com', LOCAL_DEPLOY_PATH, html)

        # Make new path
        new_path = re.search('(https:\/\/scidoggames\.com\/)(.*)', url).group(2)

        # Add 'index.html' to new path if not contain '.html'
        m = re.search('(.*)\.html', new_path)
        if not m:
            new_path = new_path + 'index.html'

        # Make directory if not exist
        m = re.search('(.*)\/', new_path)
        if m:
            new_dirpath = DEPLOY_PATH + '/' + m.group(1)
            if not os.path.exists(new_dirpath):
                os.makedirs(new_dirpath)

        # Write html
        f = open(DEPLOY_PATH + '/' + new_path, 'w', encoding='utf-8')
        f.write(html)
        f.close()
        print(os.path.basename(__file__) + ': Made ' + DEPLOY_PATH + '/' + new_path + '.')
