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
        print('find_ab = ', value)
        for dicts in abonents:
            if value.lower() in dicts['first_name'].lower() + ' ' + dicts['last_name'].lower() + ' ' + dicts['comment'].lower():
                text_contacts += view.print_dict1(dicts)
                view.print_dict(dicts)
                dict_count += 1
    if dict_count == 0:
        return ('There\'s no contact with this name. Try again')
    else:
        return text_contacts

def delite_contact():
    with open(path_1, 'r') as file:
        abonents: list[dict] = json.load(file)
        dict_count = 0
        find_ab = input('Enter the name of the abonent to delite: ')
        for dicts in abonents:
            if find_ab.lower() in dicts['first_name'].lower() + ' ' + dicts['last_name'].lower() + ' ' + dicts['comment'].lower():
                dict_count += 1
                print(f'Are you sure you want to remove contact: {dicts["first_name"]} {dicts["last_name"]}?')
                del_confirmation = input('for yes - press 1\nfor no - press 2:\n')
                if del_confirmation == '1':
                    abonents.remove(dicts)
                    with open(path_1, "w") as file:
                        json.dump(abonents, file) # TODO why id delite item 1 quite?
                    view.success_update()
        if dict_count == 0:
            print('There\'s no contact with this name. Try again')

def change_contact():
    with open(path_1, 'r') as file:
        abonents: list[dict] = json.load(file)
        dict_count = 0
        find_ab = input("Enter the name of the abonent to change it's data: ")
        for dicts in abonents:
            if find_ab.lower() in dicts['first_name'].lower() + ' ' + dicts['last_name'].lower() + ' ' + dicts['comment'].lower():
                dict_count += 1
                print(f'Are you sure you want to change data for contact: {dicts["first_name"]} {dicts["last_name"]}?')
                change_confirmation = input('for yes - press 1\nfor no - press 2:\n')
                if change_confirmation == '1':
                    change_data = input(f'To change the data enter the number\n1 - first_name\n2 - last_name\n3 - phone_number\n4 - comment\n:')
                    match change_data:
                        case '1': 
                            new_name = input('Enter a new first_name: ')
                            dicts["first_name"] = new_name
                        case '2': 
                            new_name = input('Enter a new last_name: ')
                            dicts["last_name"] = new_name
                        case '3': 
                            new_name = input('Enter a new phone_number: ')
                            dicts["phone_number"] = new_name
                        case '4': 
                            new_name = input('Enter a new comment: ')
                            dicts["comment"] = new_name
                    with open(path_1, "w") as file:
                        json.dump(abonents, file)
                    view.success_update()    
        if dict_count == 0:
            print('There\'s no contact with this name. Try again')

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