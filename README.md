# ImageWebConverter
This Python script converts and compresses jpg, jpeg, png, bmp and gif images to webp or avif.

## Installation
To run this code you require Python, Pip and the library "Pillow".

1. Install Python
2. Install Pip in CMD
3. pip install Pillow
4. pip install pillow_avif_plugin
5. clone this repo from github

## Usage
Run "py [path/to/ImageConverter.py]"

Help output:
usage: ImageWebConverter.py [-h] [--res RES] [--qual QUAL] [--outf OUTF] [source]

Python script to resize and compress images

positional arguments:
  source       Source files to change. Can be filepath or directory. If directory is passed, all files are converted. If no source is passed, workdir is used.

options:
  -h, --help   show this help message and exit
  --res RES    Target resolution, format number"x"number
  --qual QUAL  Target quality, format number
  --outf OUTF  Target file format, format ("webp", "avif")

## Image Resolution
https://tiny-img.com/blog/best-image-size-for-website/
