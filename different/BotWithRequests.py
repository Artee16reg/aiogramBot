import requests
import time
from config import TOKEN

API_URL: str = 'https://api.telegram.org/bot'
API_CATS_URL: str = 'https://aws.random.cat/meow'
ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('

offset: int = -2
counter: int = 0
cat_response: requests.Response
cat_link: str


def do_something() -> None:
    print('Был апдейт')


while counter < 100:
    updates = requests.get(f'{API_URL}{TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()['file']
                requests.get(f'{API_URL}{TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
    start_time = time.time()
    updates = requests.get(f'{API_URL}{TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    time.sleep(3)
    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')
    time.sleep(1)
    counter += 1
