from PIL import Image
import pillow_avif 
import os
import sys
import argparse

def convert(image_file, path, outf, qual):
    # find files that qualify as images
    if image_file.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        image_path = os.path.join(path, image_file) # get absolute path
        img = Image.open(image_path) # open file
        # resize image
        img = img.resize(target_resolution, Image.LANCZOS)

        # write image
        output_path = os.path.join(path, os.path.splitext(image_file)[0] + "."+outf)
        print(output_path)
        img.save(output_path, outf, quality=qual)
        print(f"Resized and converted to Webp: {image_file}")

# parser for argument handling
parser = argparse.ArgumentParser(description="Python script to resize and compress images")
parser.add_argument('--res', type=str, required=False, help='Target resolution', default="1024x800")
parser.add_argument('--qual', type=int, required=False, help='Target quality', default=100)
parser.add_argument('--outf', type=str, required=False, help='Target file format', default="webp")
parser.add_argument('source', type=str, help='Source files to change. If directory is passed, all files are converted. If no source is passed, workdir is used.', default=".")
args = parser.parse_args()

# grab arguments and save them
target_resolution = (int(args.res.split("x")[0]), int(args.res.split("x")[1]))
quality = args.qual
path = args.source
print(path)

# convert single image
if os.path.isfile(path):
    image_file = path
    convert(image_file,path, args.outf, args.qual)
# convert multiple images
elif os.path.isdir(path):
    image_files = os.listdir(path)
    for image_file in image_files:
        convert(image_file, path, args.outf, args.qual)
# invalid filepath
else:
    print("No such file or directory")
    exit(1)

# exit success
print("Image processing complete.")
exit(0)