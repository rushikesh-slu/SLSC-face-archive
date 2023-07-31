import os
from PIL import Image

def resize_images(input_directory, output_directory, size=(2560,1440)):
    # Make sure output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # List all files in the directory
    for filename in os.listdir(input_directory):
        # Check if the file is an image
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Open the image file
            img = Image.open(os.path.join(input_directory, filename))
            # Resize the image
            img_resized = img.resize(size, Image.ANTIALIAS)
            # Save the image to the output directory
            img_resized.save(os.path.join(output_directory, filename))

resize_images('images', 'resized_images_all')