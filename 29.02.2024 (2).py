import requests
import json

API_URL = "https://www.whenisthenextmcufilm.com/api/"

response = requests.get(API_URL)

# Проверка статуса ответа
if response.ok:

    data = json.loads(response.content)

    # Проверка наличия ключа "next_movie"
    if "next_movie" in data:
        # Извлечение информации о следующем фильме
        release_date = data["release_date"]["release_date"]
        production_type = data["next_movie"]["production_type"]
        next_movie_title = data["next_movie"]["title"]
        next_movie_release_date = data["next_movie"]["release_date"]

        # Вывод информации
        print("Дата выхода:", release_date)
        print("Тип производства:", production_type)
        print("Следующий фильм:", next_movie_title)
        print("Дата выхода следующего фильма:", next_movie_release_date)
    else:
        # Вывод сообщения об ошибке
        print("Ключ \"next_movie\" не найден в JSON-данных.")
else:
    # Вывод сообщения об ошибке
    print("Ошибка при запросе к API:", response.status_code)
