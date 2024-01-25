# Кирилл Панфилов Напишите функцию,
# которая ищет json файлы в указанной директории
# и сохраняет их содержимое в виде одноимённых pickle файлов.
import json
import os
import pickle


def find_json_files(folder):
    if not os.path.exists(folder):
        print('wrong folder')
        exit(1)
    for file in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, file)):
            if file.endswith('.json'):
                with open(os.path.join(folder, file), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                with open(os.path.join(folder, file[:-5] + '.pickle'), 'wb') as f:
                    pickle.dump(data, f, protocol=pickle.DEFAULT_PROTOCOL)


if __name__ == '__main__':
    find_json_files(os.getcwd())
    # with open('new_names.pickle', 'rb') as pick:
    #     print(pickle.load(pick))
