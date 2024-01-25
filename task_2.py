# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор
# и уровень доступа (от 1 до 7). 📌 После каждого ввода добавляйте новую информацию в JSON файл.
# 📌 Пользователи группируются по уровню доступа. 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться.

import json
import os
from datetime import datetime


def get_name_id_level(output_file):
    if os.path.exists(output_file):
        with open(output_file,'r', encoding='utf-8') as f:
            out_dict = json.load(f)
    else:
        out_dict = {}
    while True:
        name, user_id, level = input('please enter your name, user_id, level(1-7): ').split(',')
        name = name.strip()
        user_id = user_id.strip()
        level = level.strip()
        for value in out_dict.values():
            if user_id in value.keys():
                print(f'user_id {user_id} already in system')
                break
        else:
            if not out_dict.get(level):
                pairs = {user_id: name}
                out_dict[level] = pairs
            else:
                out_dict.get(level)[user_id] = name
            with open(output_file, 'w', encoding='utf-8') as out:
                json.dump(out_dict, out, indent=2)


if __name__ == '__main__':

    get_name_id_level('names.json')
