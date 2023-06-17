import requests
import os


def get_images(filename, images, params):
    os.makedirs("images", exist_ok=True)
    for image_number, image in enumerate(images):
        file_path = os.path.join("images", f"{filename}_{image_number}.png")
        response = requests.get(image, params=params)
        if response.ok:
            with open(file_path, 'wb') as file:
                file.write(response.content)