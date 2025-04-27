import requests
import json

# def test_api():
#     response = requests.get("https://reqres.in/api/users?page=2")
#     data = load.loads(response.text)
#     print(data["data"][0]["id"])


BASE_URL = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'



def test_api():
    response = requests.get(BASE_URL)
    with open(response.json(), 'r') as file:
        ff  = json.load(file)

    return ff



def test_load_json_file(filepath):
    """Загружает JSON-файл и возвращает его как Python-объект (обычно словарь или список)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:  # Важно указать encoding='utf-8' для правильной обработки
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filepath}' не найден.")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка: Файл '{filepath}' не является корректным JSON.")
        return None


# Пример использования:
file_path = test_api()  # Замените на имя вашего файла
log_data = test_load_json_file(file_path)

if log_data:
    # Дальнейшая обработка log_data
    pass # Замените на ваш код
else:
    print("Не удалось загрузить данные из файла.")

def test_filter_nested_logs(data, criteria):
    """
    Фильтрация для JSON со вложенными структурами.  Пример: {'service': {'name': '...', 'status': '...'}}
    Критерии могут быть, например: {'service.name': 'auth', 'service.status': 'OK'}
    """
    response = requests.get(BASE_URL)
    with open(response.json(), 'r') as file:
        data = json.load(file)
    filtered_logs = []
    for log_entry in data:
        match = True
        for key, value in criteria.items():
            keys = key.split('.')  # Разделяем ключ на части для доступа к вложенным полям
            current = log_entry
            try:
                for k in keys:
                    current = current.get(k)  # Используем get() для безопасного доступа
                if current != value:
                    match = False
                    break
            except AttributeError:
                match = False  # Если поле не найдено, считаем, что не совпадает
                break
            except TypeError:
                match = False # Обработка случая, когда значение None

        if match:
            filtered_logs.append(log_entry)
    return filtered_logs


#Пример использования (предполагаем, что структура JSON - как описано в docstring):
if log_data:
    filtered_services = test_filter_nested_logs(log_data, {'service.name': 'auth', 'service.status': 'OK'})
    print("Сервисы auth со статусом OK:", filtered_services)

