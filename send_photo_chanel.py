import random
import glob
import time
import os
import telegram
import argparse
from dotenv import load_dotenv
from open_and_send_files import open_and_send_files


def send_photo_tg_chanel(token_bot, chat_id, delay_time, files):
    bot = telegram.Bot(token=token_bot)
    for file in files:
        arg_path = file
        open_and_send_files(arg_path, chat_id, bot)
        time.sleep(int(delay_time))


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("--delay", help="время задержки в секундах")
    parser.add_argument("--bot_token", default=os.environ["TG_TOKEN_BOT"], help="token bot")
    parser.add_argument("--chanel_id", default=os.environ["TG_CHANEL_ID"], help="id chanel")
    args = parser.parse_args()
    token_bot = args.bot_token
    chat_id = args.chanel_id
    delay_time = args.delay if args.delay else os.getenv('DELAY', default=14400)
    files = glob.glob("images/*.png")
    while True:
        random.shuffle(files)
        send_photo_tg_chanel(token_bot, chat_id, delay_time, files)


if __name__ == '__main__':
    main()