import re
from pathlib import Path

def clear_names(file_name: str) -> list:
    """ Функция для очисти имен от лишних символов """
    # 1. Находим корень проекта (поднимаемся на уровень выше от папки src, где лежит main.py)
    project_root = Path(__file__).resolve().parent.parent
    # 2. Собираем точный абсолютный путь: Корень_Проекта / data / names.txt
    file_path = project_root / "data" / file_name

    new_names_list = list()
    with open(file_path, encoding='utf-8') as names_file:
        names_list = names_file.read().split()
        for name_item in names_list:
            new_name = ""
            for symbol in name_item:
                if symbol.isalpha():
                    new_name += symbol
            if new_name.isalpha():
                new_names_list.append(new_name)
    return new_names_list

def is_cyrillic(name_item: str) -> bool:
    """ Проверка на вхождение кириллицы в строку """
    return bool(re.search("[а-яА-Я]", name_item))


def filter_russian_names(names_list: list) -> list:
    """ Фильтрация имен на русском языке """
    new_names_list = list()
    for name_item in names_list:
        if is_cyrillic(name_item):
            new_names_list.append(name_item)
    return new_names_list


if __name__ == '__main__':
    cleared_name = clear_names("names.txt")

    print(filter_russian_names(cleared_name))