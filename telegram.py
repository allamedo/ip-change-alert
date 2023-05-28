import requests
from dotenv import dotenv_values

config = dotenv_values("/run/secrets/telegram-secrets")

bot_token = config["TELEGRAM_BOT_TOKEN"]
chat_id = config["TELEGRAM_CHAT_ID"]

def send_message(message,url):
    req_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    if len(url)>0:
        url_formated = '['+url+']('+url+')'
    else: url_formated = ''
    params = {
        'chat_id': chat_id,
        'text': message + ' \n'+ url ,
        'disable_web_page_preview': True,
    }
    response = requests.post(req_url, params=params)
    if response.status_code == 200:
        return True
    else:
        print(response.text)
        return False

def send_image(image):
    req_url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    params = {
        'chat_id': chat_id,
        'photo': image
    }
    response = requests.post(req_url, params=params)
    if response.status_code == 200:
        return True
    else:
        return False

if __name__ == "__main__":
    print

    #send_image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/240px-Telegram_logo.svg.png")
    send_message("Telegram Logo","https://es.m.wikipedia.org/wiki/Archivo:Telegram_logo.svg")