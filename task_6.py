# Задание No6
# 📌 Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# 📌 Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# 📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
import csv
import os
import pickle


def pickle_to_csv(pickle_file):
    if not os.path.exists(pickle_file):
        print('wrong file')
        exit(1)
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)
    with open(pickle_file[:-7] + '.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(data[0].keys())
        for item in data:
            writer.writerow(item.values())

if __name__ == '__main__':

    pickle_to_csv('new_names.pickle')