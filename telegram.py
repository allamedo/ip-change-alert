from telethon import TelegramClient, events, sync
import os


api_id = os.environ.get('TELEGRAM_API_ID') 
api_hash = os.environ.get('TELEGRAM_API_HASH')
bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
chat_id = os.environ.get('TELEGRAM_CHAT_ID')

client = TelegramClient('myclient', api_id, api_hash).start(bot_token=bot_token)
client.start()

def send_message(message,url):
    client.send_message(chat_id, '**'+message+'** '+url, link_preview=False)

def send_image(thumb):
    client.send_file(chat_id, thumb)

if __name__ == "__main__":
    send_image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/240px-Telegram_logo.svg.png")
    send_message("Telegram Logo","https://es.m.wikipedia.org/wiki/Archivo:Telegram_logo.svg")