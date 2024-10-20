import requests
import time
import json

access_token = ''
owner_id = '-189112841'
# URL для запроса к API
url = 'https://api.vk.com/method/wall.get'
# Параметры запроса
params = {
    'access_token': access_token,
    'v': '5.131',  # Версия API
    'owner_id': owner_id,  # ID сообщества
    'count': 100,  # Максимум 100 записей за раз
    'offset': 0  # Смещение для следующей порции записей
}
# Функция для получения всех записей со стены
def get_all_posts():
    all_posts = []
    while True:
        response = requests.get(url, params=params).json()
        posts = response['response']['items']
        all_posts.extend(posts)
        print(f"Загружено {len(posts)} записей, всего: {len(all_posts)}")
        if len(posts) < 100:
            break
        params['offset'] += 100
        time.sleep(1)   # чтобы избежать блокировки из-за частых запросов
    return all_posts
# Функция для сохранения данных в JSON
def save_to_json(data, filename='posts.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Данные успешно сохранены в {filename}")

posts = get_all_posts()
# Сохранение в JSON
save_to_json(posts, 'community_wall_posts.json')
# Пример вывода количества постов
print(f"Всего постов загружено: {len(posts)}")
