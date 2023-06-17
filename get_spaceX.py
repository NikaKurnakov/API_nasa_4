import requests
import argparse
import load_image


def get_one_launch(params):
    spacex_url = "https://api.spacexdata.com/v5/launches/"
    response = requests.get(spacex_url, params=params)
    if response.ok:
        received_images = response.json()
        for image in reversed(received_images):
            image_path = image['links']['flickr']['original']
            if image_path:
                return image_path
            

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", help="id интересующей картинки")
    args = parser.parse_args()
    params = {'id': args.id} if args.id else {}
    spacex_images = get_one_launch(params)
    load_image.get_images('spaceX_image', spacex_images, params)


if __name__ == '__main__':
    main()