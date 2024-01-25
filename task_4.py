# 📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 📌
# Дополните id до 10 цифр незначащими нулями. 📌 В именах первую букву сделайте прописной. 📌
# Добавьте поле хеш на основе имени и идентификатора. 📌 Получившиеся записи сохраните в json файл,
# где каждая строка csv файла представлена
# как отдельный json словарь. 📌 Имя исходного и конечного файлов передавайте как аргументы функции.
import csv
import json
import os


def csv_to_json(in_csv, out_json):
    with open(in_csv, 'r', encoding='utf-8') as c_f:
        csv_file = csv.reader(c_f)
        csv_list = []
        out_list = []
        for line in csv_file:
            csv_list.append(line)
        for items in csv_list[1:]:
            out_json_dict = {'name': items[0].title(), 'id': items[1].zfill(10), 'level': items[2],
                             'hash': str(hash((items[0] + items[1])))}
            out_list.append(out_json_dict)
        with open(out_json, 'w', encoding='utf') as f:
            json.dump(out_list, f, indent=2)


if __name__ == '__main__':
    csv_to_json('names.csv', 'new_names.json')

    # with open('new_names.json', 'r') as f:
    #     print(json.load(f))
