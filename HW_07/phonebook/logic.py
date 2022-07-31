from ast import Import
import json
from importlib.resources import path
import os
import view


FILE_NAME = 'contacts_book.json'
path = 'HW_07' + os.sep + 'phonebook' + os.sep + f'{FILE_NAME}'

def add_contact ():
    first_name = input('Enter the first name: ')
    last_name = input('Enter the last name: ')
    phone_num = input('Enter a phone number: ')
    comment = input('Enter a comment: ')
    abonent = {'first_name': first_name, 'last_name': last_name, 'phone_number': phone_num, 'comment' : comment}
    with open (path, "r") as file:
        # abonents: list = json.load(file)
        if os.stat(path).st_size == 0:
            abonents = []
        else: abonents: list = json.load(file)
    with open(path, "w") as file:
        abonents.append(abonent)
        json.dump(abonents, file)
    view.success_update()

def find_contact():
    with open(path, 'r') as file:
        abonents: list[dict] = json.load(file)
        dict_count = 0
        # while dict_count < 1: TODO add while search
        find_ab = input('Enter the name of the abonent to find: ')
        for dicts in abonents:
            if find_ab.lower() in dicts['first_name'].lower() + ' ' + dicts['last_name'].lower():
                view.print_dict(dicts)
                dict_count += 1
        if dict_count == 0:
            print('There\'s no contact with this name. Try again')

def delite_contact():
    with open(path, 'r') as file:
        abonents: list[dict] = json.load(file)
        dict_count = 0
        find_ab = input('Enter the name of the abonent to delite: ')
        for dicts in abonents:
            if find_ab.lower() in dicts['first_name'].lower() + ' ' + dicts['last_name'].lower():
                dict_count += 1
                print(f'Are you sure you want to remove contact: {dicts["first_name"]} {dicts["last_name"]}?')
                del_confirmation = input('for yes - press 1\nfor no - press 2:\n')
                if del_confirmation == '1':
                    abonents.remove(dicts)
                    with open(path, "w") as file:
                        json.dump(abonents, file) # TODO why id delite item 1 quite?
                    view.success_update()
        if dict_count == 0:
            print('There\'s no contact with this name. Try again')

def change_contact():
    with open(path, 'r') as file:
        abonents: list[dict] = json.load(file)
        dict_count = 0
        find_ab = input("Enter the name of the abonent to change it's data: ")
        for dicts in abonents:
            if find_ab.lower() in dicts['first_name'].lower() + ' ' + dicts['last_name'].lower():
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
                    with open(path, "w") as file:
                        json.dump(abonents, file)
                    view.success_update()    
        if dict_count == 0:
            print('There\'s no contact with this name. Try again')
                        
                        






# d = [{"first_name": "Maria", "last_name": "Aksenova", "phone_number": "89078909887", "comment": "no"}, {"first_name": "Anya", "last_name": "Rihter", "phone_number": "89055567788", "comment": "friend"}]
# # find_ab = 'Mar'
# for dicts in d:
# #     if find_ab in dicts['first_name'] + ' ' + dicts['last_name']: # TODO add lower search
# #         print('pop')
# #         d.remove(dicts)

#     print(dicts["first_name"], dicts['last_name'])