import json
import os
import view
import csv


FILE_NAME = 'contacts_book.json'
FILE_NAME_2 = 'contacts_book.csv'
path_1 = 'HW_08' + os.sep + 'phonebook' + os.sep + 'data' + os.sep +f'{FILE_NAME}'
path_2 = 'HW_08' + os.sep + 'phonebook' + os.sep + 'data' + os.sep + f'{FILE_NAME_2}'

def add_contact (abonent):
    # first_name = input('Enter the first name: ')
    # last_name = input('Enter the last name: ')
    # phone_num = input('Enter a phone number: ')
    # comment = input('Enter a comment: ')
    # abonent = {'first_name': first_name, 'last_name': last_name, 'phone_number': phone_num, 'comment' : comment}
    with open (path_1, "r") as file:
        if os.stat(path_1).st_size == 0:
            abonents = []
        else: abonents: list = json.load(file)
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
                text_contacts += view.print_dict1(dicts)
                view.print_dict(dicts)
                dict_count += 1
    if dict_count == 0:
        return ('There\'s no contact with this name. Try again')
    else:
        return text_contacts

def delete_contact(value_1, value_2):
    with open(path_1, 'r') as file:
        abonents: list[dict] = json.load(file)
        print(value_1, value_2)
        for dicts in abonents:
            if value_1.lower() == dicts['first_name'].lower() and value_2.lower() == dicts['last_name'].lower():
                print(dicts)
                abonents.remove(dicts)
                with open(path_1, "w") as file:
                    json.dump(abonents, file) # TODO why id delite item 1 quite?
                view.success_update()


def change_contact(abonent: dict):
    with open(path_1, 'r') as file:
        abonents: list[dict] = json.load(file)
        print(abonent)
        for dicts in abonents:
            for key in dicts[key]:
                if dicts[key] in abonent.values():
                    print(dicts)
                    dicts = abonent
                    print(dicts)
        with open(path_1, "w") as file:
            json.dump(abonents, file)
        view.success_update()    


def export_contacts_to_csv():
    with open (path_1, 'r') as file:
        data_json: list[dict] = json.load(file)
    with open (path_2, 'w') as file:
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

# find_contact('aks')