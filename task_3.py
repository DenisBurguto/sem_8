# fuction to save json to csv from task_2
import json
import os
import csv


def save_json_to_csv(input, output):
    if os.path.exists(input):
        with open(input, 'r', encoding='utf-8') as f:
            json_dict = json.load(f)
        users = []
        for u_lvl, user in json_dict.items():
            for u_id, u_name in user.items():
                users.append((u_name, u_id, u_lvl))
        with (open(output, 'w', newline='', encoding='utf-8') as c_f):
            writer = csv.writer(c_f, dialect='excel')
            writer.writerow(['Name', 'ID', 'Level'])
            for user in users:
                writer.writerow(user)

    else:
        print('wrong path to file')

if __name__ == '__main__':


    save_json_to_csv('names.json', 'names.csv')
