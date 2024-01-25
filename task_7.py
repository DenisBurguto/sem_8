# Задание No7
# 📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Распечатайте его как pickle строку.


import csv
import os
import pickle


def csv_to_pickle(csv_file):
    if not os.path.exists(csv_file):
        print('wrong file')
        exit(1)
    with open(csv_file, 'r', encoding='utf-8') as f:
        data = list(csv.reader(f))
        print(f'{pickle.dumps(data, protocol=pickle.DEFAULT_PROTOCOL)}')


if __name__ == '__main__':
    csv_to_pickle('new_names.csv')