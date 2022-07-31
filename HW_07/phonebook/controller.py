import view
import logic

def phonebook_create() -> None:
    command = view.get_command()
    while command not in ['1', '2', '3', '4', '5']:
        command = view.get_command()
    if command == '1':
        logic.add_contact()
    elif command == '2':
        logic.find_contact()
    elif command == '3':
        logic.delite_contact()
    elif command == '4':
        logic.change_contact()
    elif command == '5':
        logic.export_contacts_to_csv()

