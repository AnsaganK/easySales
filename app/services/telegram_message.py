import requests

from constants import BOT_TOKEN


# BOT_TOKEN = getenv('BOT_TOKEN')

def send_verification_code(user_verification_code) -> bool:
    code = user_verification_code.code
    user = user_verification_code.user

    telegram_id = user.profile.telegram_id
    if not telegram_id:
        return False
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': telegram_id,
        'text': f'Ваш код для входа: {code} \nНе сообщайте его никому'
    }
    r = requests.post(url, data=payload)
    return r.status_code == 200


def send_message(chat_ids: list, message: str):
    for chat_id in chat_ids:
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        payload = {
            'chat_id': chat_id,
            'text': f'{message}'
        }
        r = requests.post(url, data=payload)
        return r.status_code == 200
