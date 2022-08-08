
def get_command():
    command = input(
        'Choose a command for the phonebook: \n1 - Add a new contact\n2 - Find a contact\n3 - Delete a contact\n4 - Change a contact\n5 - Convert your data to .csv:\n')
    return command

def print_dict(name_dict: str) -> None:
    print(f'Contact\'s information: ')
    for i in name_dict:
        print(f'    {i}: {name_dict[i]}')

def dict_to_str(name_dict: str) -> None:
    cont_text = f'\n'
    for i in name_dict:
        cont_text += i + ": " + name_dict[i] + f"\n"
    return cont_text

def success_update():
    print('The data has been successfully updated!')

def success_saved():
    print('The data has been successfully saved!')

