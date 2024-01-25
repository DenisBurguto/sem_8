# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее файла новый
# с данными в формате JSON. 📌 Имена пишите с большой буквы. 📌 Каждую пару сохраняйте с новой строки.
import json


def from_txt_to_json(in_file, out_file):
    pairs = {}
    with open(in_file, 'r', encoding='utf-8') as f:
        for pair in f:
            key, value = pair.split(' | ')
            pairs[key.title()] = float(value)
    with open(out_file, 'w', encoding='utf-8') as out:
        json.dump(pairs, out, indent=1)

if __name__ == '__main__':

    from_txt_to_json('../sem_7/sample/res_file.txt', 'out_file.json')
