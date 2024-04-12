#!/usr/bin/python
# coding: utf-8
# (c) 2021 Mineyuki Iwasaki

import os
import re
import sys

DEPLOY_PATH = sys.argv[1]
#JPEG, PNG, GIF, TIFF, and even some less common ones like HEIC and WebP.
EXTENSIONS = ('.ico', '.svg', '.bmp', '.hdr', '.jpg', '.png', '.psd', '.tga')
SOURCE_PATH = 'images'

# Find all html
for root, _, files in os.walk(SOURCE_PATH):
    for file in files:
        base, ext = os.path.splitext(file)
        if ext.lower() not in EXTENSIONS:
            continue

        # Make directory if not exist
        dir_path = os.path.join(DEPLOY_PATH, root)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        if ext.lower() == '.ico' or ext.lower() == '.svg':
            os.system(f'cp -f {os.path.join(root, file)} {os.path.join(dir_path, file)}')
            print(f'Copied to {os.path.join(dir_path, file)}')
            continue

        width = int(re.search('(.*?)-([0-9]+)x([0-9]+)-([0-9]+)', base).group(2))
        height = int(re.search('(.*?)-([0-9]+)x([0-9]+)-([0-9]+)', base).group(3))
        large_width = int(re.search('(.*?)-([0-9]+)x([0-9]+)-([0-9]+)', base).group(4))
        large_height = int(large_width * height / width)
        medium_width = int(large_width / 2)
        medium_height = int(large_height / 2)
        small_width = int(large_width / 4)
        small_height = int(large_height / 4)
        base = re.search('(.*?)-([0-9]+)x([0-9]+)-([0-9]+)', base).group(1)

        input_file = os.path.join(root, file)
        output_file = os.path.join(dir_path, f'{base}-{large_width}x{large_height}.webp')
        #large_output_file = os.path.join(dir_path, f'{base}-large.webp')
        #medium_output_file = os.path.join(dir_path, f'{base}-medium.webp')
        #small_output_file = os.path.join(dir_path, f'{base}-small.webp')


        #large_width = int(large_width/4)
        #large_height = int(large_height/4)

        os.system(f'magick {input_file} -define webp:method=6 -quality 50 -thumbnail {large_width}x{large_height} {output_file}')
        #os.system(f'magick {input_file} -define webp:method=6 -quality 50 -thumbnail {large_width}x{large_height} {large_output_file}')
        #os.system(f'magick {input_file} -define webp:method=6 -quality 50 -thumbnail {medium_width}x{medium_height} {medium_output_file}')
        #os.system(f'magick {input_file} -define webp:method=6 -quality 50 -thumbnail {small_width}x{small_height} {small_output_file}')
        input_file_size = os.path.getsize(input_file)
        output_file_size = os.path.getsize(output_file)
        #large_output_file_size = os.path.getsize(large_output_file)
        #medium_output_file_size = os.path.getsize(medium_output_file)
        #small_output_file_size = os.path.getsize(small_output_file)
        print(f'Converted to {output_file} {input_file_size / 1000:.2f}kb -> {output_file_size / 1000:.2f}kb' + \
            f' ({100 * output_file_size / input_file_size:.2f}%)')
        #print(f'Converted to {large_output_file} {input_file_size / 1000:.2f}kb -> {large_output_file_size / 1000:.2f}kb' + \
        #    f' ({100 * large_output_file_size / input_file_size:.2f}%)')
        #print(f'Converted to {medium_output_file} {input_file_size / 1000:.2f}kb -> {medium_output_file_size / 1000:.2f}kb' + \
        #    f' ({100 * medium_output_file_size / input_file_size:.2f}%)')
        #print(f'Converted to {small_output_file} {input_file_size / 1000:.2f}kb -> {small_output_file_size / 1000:.2f}kb' + \
        #    f' ({100 * small_output_file_size / input_file_size:.2f}%)')
