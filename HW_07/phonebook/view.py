def get_command():
    command = input('Choose a command for the phonebook: \n1 - Add a new contact\n2 - Find a contact\n3 - Delete a contact\n4 - Change a contact\n: ')
    return command

def print_dict(name_dict: str) -> None:
    print(f'Contact\'s information: ')
    for i in name_dict:
        print(f'    {i}: {name_dict[i]}')

def success_update():
    print('Tha data has been successfully updated!')