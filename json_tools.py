import json
import os
from typing import Any


def load(file_path: str, encoding: str = 'utf-8') -> Any:
    """ Прочитать данные из json-файла """
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        return None
    with open(file_path, encoding=encoding) as file:
        data = json.load(file)
    return data


def save(file_path: str, data: Any, mode: str = 'w', encoding: str = 'utf8') -> None:
    """ Записать данные в json-файл """
    with open(file_path, mode=mode, encoding=encoding) as file:
        json.dump(data, file)
