#!/usr/bin/python
# coding: utf-8
# (c) 2021 Mineyuki Iwasaki

import os
import re

DEPLOY_PATH = "docs"

# Find all html, css, js, xml and svg
for root, _, files in os.walk(DEPLOY_PATH):
    for file in files:
        base, ext = os.path.splitext(file)
        if ext != ".html" and ext != ".css" and ext != ".js" and ext != ".xml" and ext != ".svg":
            continue

        # Read html, css, js, xml or svg
        file_path = os.path.join(root, file)
        f = open(file_path, "r", encoding="utf-8")
        original_content = f.read()
        f.close()

        # Optimize html or xml
        if ext == ".html" or ext == ".xml":
            # Remove comments
            content = re.sub(r"<!\-\-.*?\-\->", "", original_content, flags=re.DOTALL)
            # Remove spaces
            content = re.sub(r" +", " ", content)
            content = re.sub(r"^\s+", "", content, flags=re.MULTILINE)

        # Optimize css
        if ext == ".css":
            # Remove comments
            content = re.sub(r"\/\*.*?\*\/", "", original_content, flags=re.DOTALL)
            # Remove spaces
            content = re.sub(r" +", " ", content)
            content = re.sub(r"^\s+", "", content, flags=re.MULTILINE)
            content = re.sub(r"\s*\+\s*", "+", content)
            content = re.sub(r"\s*\-\s*", "-", content)
            content = re.sub(r"\s*\*\s*", "*", content)
            content = re.sub(r"\s*\/\s*", "/", content)
            content = re.sub(r"\s*,\s*", ",", content)
            content = re.sub(r"\s*:\s*", ":", content)
            content = re.sub(r"\s*;\s*", ";", content)
            content = re.sub(r"\s*\(\s*", "(", content)
            content = re.sub(r"\s*\)\s*", ")", content)
            content = re.sub(r"\s*\{\s*", "{", content)
            content = re.sub(r"\s*\} *", "}", content)

        # Optimize js
        if ext == ".js":
            # Remove comments
            content = re.sub(r"\/\*.*?\*\/", "", original_content, flags=re.DOTALL)
            content = re.sub(r"\/\/.*$", "", content, flags=re.MULTILINE)
            # Remove spaces
            content = re.sub(r" +", " ", content)
            content = re.sub(r"^\s+", "", content, flags=re.MULTILINE)
            content = re.sub(r"\s*=\s*", "=", content)
            content = re.sub(r"\s*<\s*", "<", content)
            content = re.sub(r"\s*>\s*", ">", content)
            content = re.sub(r"\s*\+\s*", "+", content)
            content = re.sub(r"\s*\-\s*", "-", content)
            content = re.sub(r"\s*\*\s*", "*", content)
            content = re.sub(r"\s*\/\s*", "/", content)
            content = re.sub(r"\s*,\s*", ",", content)
            content = re.sub(r"\s*; *", ";", content)
            content = re.sub(r"\s*\(\s*", "(", content)
            content = re.sub(r"\s*\)\s*", ")", content)
            content = re.sub(r" *\{ *", "{", content)
            content = re.sub(r" *\} *", "}", content)

        # Optimize svg
        if ext == ".svg":
            # Remove unused elements
            content = re.sub(r"<\?xml.*?\?>", "", original_content, flags=re.DOTALL)
            content = re.sub(r"<defs.*?\/>", "", content, flags=re.DOTALL)
            content = re.sub(r"<metadata.*?<\/metadata>", "", content, flags=re.DOTALL)
            content = re.sub(r"<sodipodi:namedview.*?<\/sodipodi:namedview>", "", content, flags=re.DOTALL)
            content = re.sub(r"<title>.*?<\/title>", "", content, flags=re.DOTALL)
            content = re.sub(r"^\s*id=\".*?\"", "", content, flags=re.MULTILINE)
            content = re.sub(r"^\s*inkscape:connector-curvature=\".*?\"", "", content, flags=re.MULTILINE)
            content = re.sub(r"^\s*inkscape:export-filename=\".*?\"", "", content, flags=re.MULTILINE)
            content = re.sub(r"^\s*inkscape:export-xdpi=\".*?\"", "", content, flags=re.MULTILINE)
            content = re.sub(r"^\s*inkscape:export-ydpi=\".*?\"", "", content, flags=re.MULTILINE)
            content = re.sub(r"^\s*inkscape:groupmode=\".*?\"", "", content, flags=re.MULTILINE)
            content = re.sub(r"^\s*inkscape:label=\".*?\"", "", content, flags=re.MULTILINE)
            content = re.sub(r"^\s*inkscape:version=\".*?\"", "", content, flags=re.MULTILINE)
            content = re.sub(r"^\s*sodipodi:docname=\".*?\"", "", content, flags=re.MULTILINE)
            content = re.sub(r"^\s*sodipodi:nodetypes=\".*?\"", "", content, flags=re.MULTILINE)
            content = re.sub(r"^\s*version=\".*?\"", "", content, flags=re.MULTILINE)
            content = re.sub(r"^\s*xmlns:cc=\".*?\"", "", content, flags=re.MULTILINE)
            content = re.sub(r"^\s*xmlns:dc=\".*?\"", "", content, flags=re.MULTILINE)
            content = re.sub(r"^\s*xmlns:inkscape=\".*?\"", "", content, flags=re.MULTILINE)
            content = re.sub(r"^\s*xmlns:rdf=\".*?\"", "", content, flags=re.MULTILINE)
            content = re.sub(r"^\s*xmlns:sodipodi=\".*?\"", "", content, flags=re.MULTILINE)
            content = re.sub(r"^\s*xmlns:svg=\".*?\"", "", content, flags=re.MULTILINE)
            # Remove spaces
            content = re.sub(r"\n", " ", content)
            content = re.sub(r"<", "\n<", content)
            content = re.sub(r">", ">\n", content)
            content = re.sub(r"\s*> *", ">", content)
            content = re.sub(r"\s*\/> *", "/>", content)
            content = re.sub(r" +", " ", content)
            content = re.sub(r"^\s+", "", content, flags=re.MULTILINE)

        # Write html, css, js, xml or svg
        f = open(file_path, "w", encoding="utf-8")
        f.write(content)
        f.close()
        print(f"Optimized {file_path} {len(original_content)} byte -> {len(content)} byte" + \
            f" ({100 * len(content) / len(original_content):.2f} %)")

# Find all jpg or png
for root, _, files in os.walk(DEPLOY_PATH):
    for file in files:
        base, ext = os.path.splitext(file)
        if ext != ".jpg" and ext != ".png":
            continue

        # Remove jpg or png
        file_path = os.path.join(root, file)
        os.remove(file_path)
        print(f"Removed {file_path}")
