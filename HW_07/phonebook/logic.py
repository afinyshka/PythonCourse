import json
from importlib.resources import path
import os


FILE_NAME = 'contacts_book.json'
path = 'HW_07' + os.sep + 'phonebook' + os.sep + f'{FILE_NAME}'

def add_contact ():
    first_name = input('Enter the first name: ')
    last_name = input('Enter the last name: ')
    phone_num = input('Enter a phone number: ')
    comment = input('Enter a comment: ')
    abonent = {'first_name': first_name, 'last_name': last_name, 'phone_number': phone_num, 'comment' : comment}
    with open (path, "r") as file:
        abonents: list = json.load(file)
    with open(path, "w") as file:
        abonents.append(abonent)
        json.dump(abonents, file)
    #     я закоментил сохранение в txt и csv потому что смысла нет, лучше хранить в одном месте
    #     а если надо будет выгрузить в другой формат, то лучше это делать через функцию.
    # with open ('HW_07' + os.sep + 'phonebook' + os.sep + 'phonebook.txt', "a") as file:
    #     file.write(f'{abonent}\n')
    # with open ('HW_07' + os.sep + 'phonebook' + os.sep + 'phonebook.csv', "a") as file:
    #     file.write(f'{abonent}\n')


def find_contact(first_name: str, last_name: str):
    with open(path, 'r') as file:
        abonents: list[dict] = json.load(file)
        # TODO: реализовать поиск нужного контакта в списке контактов abonents
        return