import requests

from env import BOT_TOKEN

def send_message(message, chat_id, reply_markup=None):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML',
    }

    # set keyboard if exists
    if reply_markup:
        payload['reply_markup'] = {
            'keyboard': reply_markup,
            'resize_keyboard': True,
            'one_time_keyboard': True
        }

    response = requests.post(url, json=payload)

    print(response.json())

    return response.json()