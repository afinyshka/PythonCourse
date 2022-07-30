import view
import logic

def phonebook_create() -> None:
    command = view.get_command()
    while command not in ['1', '2', '3', '4']:
        command = view.get_command()
    if command == '1':
        logic.add_contact()
        # f \n1 - Add a new contact\n2 - Find a contact\n 3 - Delete a contact'
    elif command == '2':
        logic.find_contact()
    elif command == '3':
        logic.delite_contact()
    elif command == '4':
        logic.change_contact()

