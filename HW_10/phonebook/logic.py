import json
import os
import view
import csv

from HW_10.config import BASE_PATH

FILE_NAME = 'contacts_book.json'
FILE_NAME_2 = 'contacts_book.csv'
path_1 = BASE_PATH / 'phonebook' / 'data' / f'{FILE_NAME}'
# path_1 = '/Users/user/Desktop/GB/Python_Course/HW_10/phonebook/data/contacts_book.json'
path_2 = BASE_PATH / 'phonebook' / 'data' / f'{FILE_NAME_2}'


cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

def add_contact(abonent):
    with open(path_1, "r") as file:
        if os.stat(path_1).st_size == 0:
            abonents = []
        else:
            abonents: list = json.load(file)
    with open(path_1, "w") as file:
        abonents.append(abonent)
        json.dump(abonents, file)
    view.print_dict(abonent)
    view.success_saved()


def find_contact(value):
    with open(path_1, 'r') as file:
        abonents: list[dict] = json.load(file)
        dict_count = 0
        text_contacts = ''
        for dicts in abonents:
            if value.lower() in dicts['first_name'].lower() + ' ' + dicts['last_name'].lower() + ' ' + dicts['comment'].lower():
                text_contacts += view.dict_to_str(dicts)
                view.print_dict(dicts)
                dict_count += 1
    if dict_count == 0:
        return ('There\'s no contact with this name. Try again')
    else:
        return text_contacts


def delete_contact(value_1, value_2):
    with open(path_1, 'r') as file:
        abonents: list[dict] = json.load(file)
        for dicts in abonents:
            if value_1.lower() == dicts['first_name'].lower() and value_2.lower() == dicts['last_name'].lower():
                abonents.remove(dicts)
                with open(path_1, "w") as file:
                    json.dump(abonents, file)
                view.success_update()


def change_contact(val_1, val_2, new_abonent: dict):
    with open(path_1, 'r') as file:
        abonents: list[dict] = json.load(file)
        dict_match = 0
        for dicts in abonents:
            if val_1.lower() == dicts['first_name'].lower() and val_2.lower() == dicts['last_name'].lower():
                dict_match += 1
                abonents.remove(dicts)
        abonents.append(new_abonent)
        with open(path_1, "w") as file:
            json.dump(abonents, file)
        view.success_update()


def export_contacts_to_csv():
    with open(path_1, 'r') as file:
        data_json: list[dict] = json.load(file)
    with open(path_2, 'w') as file:
        writer: list[dict] = csv.writer(file)
        writer.writerow(
            [
                'first_name',
                'last_name',
                'phone_number',
                'comment'
            ]
        )
        writer = csv.writer(file)
        for dicts in data_json:
            writer.writerow(
                [
                    dicts["first_name"],
                    dicts["last_name"],
                    dicts["phone_number"],
                    dicts["comment"]
                ]
            )
    view.success_saved()


