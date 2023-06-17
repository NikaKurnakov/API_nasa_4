import telegram
import argparse
import random
import glob
from open_and_send_files import open_and_send_files
from dotenv import load_dotenv
import os


def send_photo(token_bot, chat_id, arg_path):
    bot = telegram.Bot(token=token_bot)
    bot.send_message(chat_id=chat_id, text='Привет!')
    open_and_send_files(arg_path, chat_id, bot)


def main():
    load_dotenv()
    files = glob.glob("images/*.png")
    parser = argparse.ArgumentParser()
    parser.add_argument("--bot_token", default=os.environ["TG_TOKEN_BOT"], help="token bot")
    parser.add_argument("--chanel_id", default=os.environ["TG_CHANEL_ID"], help="id chanel")
    parser.add_argument("--file", help="интересующий файл")
    args = parser.parse_args()
    token_bot = args.bot_token
    chat_id = args.chanel_id
    file_name = os.path.join("images", args.file)
    arg_path = file_name if args.file else f"{random.choice(files)}"
    send_photo(token_bot, chat_id, arg_path)


if __name__ == '__main__':
    main()
