import sys
import os
import controller
from menu import *


def main():
    os.system('clear')
    tasks_archive = controller.create_tasks_archive()

    program_active = True
    while program_active:
        display_welcome_text()
        display_commands_menu()

        option = input('Select an option: ')
        os.system('clear')

        if option == '1':
            controller.ask_add_item(tasks_archive)
        elif option == '2':
            controller.ask_modify_item(tasks_archive)
        elif option == '3':
            controller.ask_delete_item(tasks_archive)
        elif option == '4':
            controller.mark_selected_item(tasks_archive)
        elif option == '5':
            controller.display_all_items(tasks_archive)
        elif option == '6':
            controller.display_item(tasks_archive)
        elif option == '7':
            controller.export_tasks_to_file(tasks_archive)
        elif option == '0':
            sys.exit()
        input('\nPress enter to continue...')
        os.system('clear')


if __name__ == '__main__':
    main()
