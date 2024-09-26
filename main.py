def evaluate_algorithm_complexity():
    # Оценка сложности
    complexity = {
        "Initialization": "O(1)",  # Инициализация бота и диспетчера
        "Keyboard Creation": "O(1)",  # Создание клавиатуры
        "Database Connection": "O(1)",  # Подключение к БД
        "Create Users Table": "O(1)",  # Создание таблицы пользователей
        "Create Favorites Table": "O(1)",  # Создание таблицы избранных
        "Start Command Handling": "O(1)",  # Обработка команды /start
        "User Registration": {
            "Find User": "O(1)",  # Поиск пользователя
            "Insert User": "O(1)",  # Вставка пользователя
        },
        "Send Tips": "O(1)",  # Отправка советов
        "Search Artworks": {
            "Set State": "O(1)",  # Установка состояния
            "Translate Query": "O(1)",  # Перевод запроса
            "Fetch Artworks": "O(1)",  # Запрос на получение произведений
            "Process Artworks": {
                "Get Artwork Info": "O(1)",  # Получение информации о произведении
                "Translate Title": "O(1)",  # Перевод названия
                "Construct Response": "O(m)",  # Формирование ответа, где m - количество найденных произведений
            }
        },
        "Get Artwork Info": {
            "Fetch Artwork Details": "O(1)",  # Получение деталей произведения
            "Send Artwork Info": "O(1)",  # Отправка информации о произведении
        },
        "Add to Favorites Confirmation": {
            "Insert Favorite": "O(1)",  # Вставка в избранное
        },
        "View Favorites": {
            "Fetch Favorites": "O(1)",  # Получение избранных произведений
            "Construct Response": "O(n)",  # Формирование ответа, где n - количество избранных произведений
        },
        "Main Loop": "O(1)",  # Основной цикл
    }

    # Вывод оценки сложности
    print("Оценка сложности алгоритма:")
    for operation, complexity_value in complexity.items():
        if isinstance(complexity_value, dict):
            print(f"{operation}:")
            for sub_operation, sub_complexity in complexity_value.items():
                print(f"  - {sub_operation}: {sub_complexity}")
        else:
            print(f"{operation}: {complexity_value}")

if __name__ == "__main__":
    evaluate_algorithm_complexity()