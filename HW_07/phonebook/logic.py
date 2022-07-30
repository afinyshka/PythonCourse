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
    with open (path, "a") as file:
        file.write(f'{abonent}\n')
    with open ('HW_07' + os.sep + 'phonebook' + os.sep + 'phonebook.txt', "a") as file:
        file.write(f'{abonent}\n')
    with open ('HW_07' + os.sep + 'phonebook' + os.sep + 'phonebook.csv', "a") as file:
        file.write(f'{abonent}\n')
