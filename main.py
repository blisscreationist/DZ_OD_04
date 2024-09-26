def evaluate_algorithm_complexity():
    # Оценка сложности
    print("# Оценка сложности алгоритма\n")

    complexity = {
        "Initialization": ("O(1)", "Константная сложность, так как время выполнения не зависит от размера входных данных."),
        "Keyboard Creation": ("O(1)", "Константная сложность, так как создание клавиатуры выполняется за постоянное время."),
        "Database Connection": ("O(1)", "Константная сложность, так как подключение к базе данных выполняется за постоянное время."),
        "Create Users Table": ("O(1)", "Константная сложность, так как создание таблицы выполняется за постоянное время, независимо от количества данных."),
        "Create Favorites Table": ("O(1)", "Константная сложность, так как создание таблицы выполняется за постоянное время."),
        "Start Command Handling": ("O(1)", "Константная сложность, так как ответ на команду выполняется за постоянное время."),
        "User Registration": {
            "Find User": ("O(1)", "Константная сложность, так как поиск пользователя выполняется за постоянное время."),
            "Insert User": ("O(1)", "Константная сложность, так как вставка пользователя выполняется за постоянное время."),
        },
        "Send Tips": ("O(1)", "Константная сложность, так как выбор и отправка совета выполняется за постоянное время."),
        "Search Artworks": {
            "Set State": ("O(1)", "Константная сложность, так как установка состояния выполняется за постоянное время."),
            "Translate Query": ("O(1)", "Константная сложность, так как перевод запроса выполняется за постоянное время."),
            "Fetch Artworks": ("O(1)", "Константная сложность, так как запрос на получение произведений выполняется за постоянное время."),
            "Process Artworks": {
                "Get Artwork Info": ("O(1)", "Константная сложность, так как получение информации о произведении выполняется за постоянное время."),
                "Translate Title": ("O(1)", "Константная сложность, так как перевод названия выполняется за постоянное время."),
                "Construct Response": ("O(m)", "Время выполнения пропорционально количеству найденных произведений при обработке результатов."),
            }
        },
        "Get Artwork Info": {
            "Fetch Artwork Details": ("O(1)", "Константная сложность, так как запрос деталей произведения выполняется за постоянное время."),
            "Send Artwork Info": ("O(1)", "Константная сложность, так как отправка информации о произведении выполняется за постоянное время."),
        },
        "Add to Favorites Confirmation": {
            "Insert Favorite": ("O(1)", "Константная сложность, так как вставка в таблицу выполняется за постоянное время."),
        },
        "View Favorites": {
            "Fetch Favorites": ("O(n)", "Линейная сложность, так как необходимо получить все избранные произведения и сформировать ответ."),
            "Construct Response": ("O(n)", "Время выполнения пропорционально количеству избранных произведений."),
        },
        "Main Loop": ("O(1)", "Константная сложность, так как основной цикл выполняет постоянное количество операций."),
    }

    # Вывод оценки сложности
    for operation, value in complexity.items():
        if isinstance(value, dict):
            print(f"{operation}:")
            for sub_operation, sub_value in value.items():
                if isinstance(sub_value, tuple) and len(sub_value) == 2:
                    print(f"  - {sub_operation}: {sub_value[0]}")
                    print(f"    {sub_value[1]}")
                else:
                    print(f"  - {sub_operation}: {sub_value}")  # В случае, если формат не соответствует
        else:
            print(f"{operation}: {value[0]}")
            print(f"  {value[1]}")

if __name__ == "__main__":
    evaluate_algorithm_complexity()



