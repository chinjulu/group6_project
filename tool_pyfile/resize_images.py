import os
from PIL import Image

def resize_image(input_path, output_path, size):
    """
    Resize an image to the specified size.

    :param input_path: Path to the input image.
    :param output_path: Path to save the resized image.
    :param size: Tuple (width, height) for the new size.
    """
    with Image.open(input_path) as img:
        img = img.resize(size, Image.LANCZOS)
        img.save(output_path)
        print(f'Resized image saved to: {output_path}')

def resize_images_in_directory(directory, size):
    """
    Resize all images in the specified directory.

    :param directory: Path to the directory containing images.
    :param size: Tuple (width, height) for the new size.
    """
    if not os.path.exists(directory):
        print(f'Directory {directory} does not exist.')
        return

    output_directory = os.path.join(directory, 'resized')
    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(output_directory, filename)
            resize_image(input_path, output_path, size)

if __name__ == "__main__":
    # Example usage
    directory = "Assets/img/"  # Replace with your image directory
    size = (100, 100)  # Replace with the desired size

    resize_images_in_directory(directory, size)
