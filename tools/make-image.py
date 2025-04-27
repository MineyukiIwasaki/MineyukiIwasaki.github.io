#!/usr/bin/python3
# coding: utf-8
# (c) 2021 Mineyuki Iwasaki

import os
import re

DEPLOY_PATH = 'docs'
EXTENSIONS = ('.gif', '.heic', '.jpg', '.png', '.svg', '.tif', '.webp')
SOURCE_PATH = 'images'

# Find all images
for root, _, files in os.walk(SOURCE_PATH):
    for file in files:
        base, ext = os.path.splitext(file)
        if ext == '' or ext.lower() not in EXTENSIONS:
            continue

        # Make directory if not exist
        dir_path = os.path.join(DEPLOY_PATH, root)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # Copy file if svg
        if ext.lower() == '.svg':
            os.system(f'cp -f {os.path.join(root, file)} {os.path.join(dir_path, file)}')
            print(f'Generated {os.path.join(dir_path, file)}')
            continue

        # Get width and height from filename
        match = re.search('(.*?)-([0-9]+)x([0-9]+)-([0-9]+)', base)
        base = match.group(1)
        width = float(match.group(2))
        height = float(match.group(3))
        new_width = int(match.group(4))
        new_height = int(new_width * height / width)

        # Convert to webp
        input_file = os.path.join(root, file)
        input_file_size = os.path.getsize(input_file)
        output_file = os.path.join(dir_path, f'{base}.webp')
        os.system(f'magick {input_file} -define webp:method=6 -quality 50 -thumbnail {new_width}x{new_height}! {output_file}')
        output_file_size = os.path.getsize(output_file)
        print(f'Generated {output_file} {input_file_size / 1000:.2f}kb -> {output_file_size / 1000:.2f}kb' + \
            f' ({100 * output_file_size / input_file_size:.2f}%)')
