#!/usr/bin/python
# coding: utf-8
# (c) 2021 Mineyuki Iwasaki

import os
import re

SITEMAP_PATH = os.path.join("docs", "sitemap.xml")
SOURCE_PATH = "html"

# Open sitemap
f = open(SITEMAP_PATH, "w", encoding="utf-8")
f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
f.write("<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n")

# Find all html
for root, _, files in os.walk(SOURCE_PATH):
    for file in files:
        base, ext = os.path.splitext(file)
        if ext != ".html" or file == "base.html":
            continue

        # Read html
        h = open(os.path.join(root, file), "r", encoding="utf-8")
        html = h.read()
        h.close()

        # Get url from html
        url = re.search(r"<url>\s*(.*?)\s*</url>", html, flags=re.DOTALL).group(1)

        # Write url to sitemap
        f.write("    <url>\n")
        f.write(f"        <loc>{url}</loc>\n")
        f.write("    </url>\n")

# Close sitemap
f.write("</urlset>\n")
f.close()
print(f"Generated {SITEMAP_PATH}")
