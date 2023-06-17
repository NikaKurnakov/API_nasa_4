import requests
import argparse
import load_image
from datetime import datetime
import os
from dotenv import load_dotenv


def get_epic_picture(numb, params):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(epic_url, params=params)
    print(response.url)
    if response.ok:
        unpacked_response = response.json()
        epic_images = []
        image_page = unpacked_response[:numb]
        for image in image_page:
            images_name = image["image"]
            images_date = image["date"]
            if images_name and images_date:
                image_date_format = datetime.fromisoformat(images_date)
                image_date = datetime.date(image_date_format).strftime("%Y/%m/%d")
                epic_image_url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{images_name}.png"
                epic_images.append(epic_image_url)
        return epic_images


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("--epic_token", default=os.environ['NASA_EPIC_TOKEN'], help="token epic")
    parser.add_argument("--numb", default=5, help="numb picture", type=int)
    args = parser.parse_args()
    numb = args.numb
    params = {
        'api_key': args.epic_token
    }
    function_epic = get_epic_picture(numb, params)
    load_image.get_images("epic_image", function_epic, params)


if __name__ == '__main__':
    main()