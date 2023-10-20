from PIL import Image
import pillow_avif 
import os

# Set the target resolution and quality
target_resolution = (1280, 853)  # Change this to your desired resolution
quality = 75  # Change this to your desired quality (0-100)

# Input and output directories
input_directory = 'input_images'
output_directory = 'output_images'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# List all files in the input directory
image_files = os.listdir(input_directory)

for image_file in image_files:
    if image_file.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        # Open the image
        image_path = os.path.join(input_directory, image_file)
        img = Image.open(image_path)

        # Resize the image
        img = img.resize(target_resolution, Image.LANCZOS)

        # Convert the image to Webp format
        output_path = os.path.join(output_directory, os.path.splitext(image_file)[0] + ".webp")
        img.save(output_path, "webp", quality=quality)

        print(f"Resized and converted to Webp: {image_file}")

print("Image processing complete.")
