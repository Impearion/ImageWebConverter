from PIL import Image
import pillow_avif
import os
import sys
import argparse
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

# interpret resolution
def calculate_target_resolution(img, res_arg):
    if 'x' in res_arg:
        # explicit width x height
        width, height = map(int, res_arg.lower().split('x'))
        return (width, height)
    elif res_arg.isdigit():
        # only widht given → calculate height, keep aspect ratio
        target_width = int(res_arg)
        original_width, original_height = img.size
        aspect_ratio = original_height / original_width
        target_height = int(target_width * aspect_ratio)
        return (target_width, target_height)
    else:
        return img.size

# conversion
def convert(image_file, path, outf, qual, res_arg):
    if image_file.lower().endswith(image_extensions):
        image_path = os.path.join(path, image_file)
        img = Image.open(image_path)

        # calculate new resolution
        target_resolution = calculate_target_resolution(img, res_arg)

        # resize only on change
        if img.size != target_resolution:
            img = img.resize(target_resolution, Image.LANCZOS)


        output_path = os.path.join(path, os.path.splitext(image_file)[0] + "." + outf)
        img.save(output_path, outf, quality=qual)
        print(f"Resized and converted: {image_file}")

# parser for argument handling
parser = argparse.ArgumentParser(description="Python script to resize and compress images")
parser.add_argument('--res', type=str, required=False, help='Target resolution: ((width"x"height) or just width)', default="960")
parser.add_argument('--qual', type=int, required=False, help='Target quality (e.g., 80)', default=100)
parser.add_argument('--outf', type=str, required=False, help='Output format ("webp" or "avif")', default="webp")
parser.add_argument('source', type=str, nargs='?', help='File or directory path', default=".")
args = parser.parse_args()

quality = args.qual
path = args.source

# convert single image
if os.path.isfile(path):
    path_parts = os.path.split(path)
    image_file = path_parts[-1]
    dir_path = path_parts[0] or "."
    convert(image_file, dir_path, args.outf, quality, args.res)

# process directory
elif os.path.isdir(path):
    image_files = os.listdir(path)
    for image_file in image_files:
        convert(image_file, path, args.outf, quality, args.res)

# invalid filepath
else:
    print("No such file or directory")
    exit(1)

print("Image processing complete.")
exit(0)
