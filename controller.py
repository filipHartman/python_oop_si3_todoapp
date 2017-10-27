from model import *


def ask_add_item(tasks_archive):
    name = input('Enter the name of task to do: ')
    description = input('Enter the description of task to do: ')
    task = ToDo_item(name, description)
    tasks_archive.todo_archive.append(task)

def ask_delete_item():
    pass


def ask_modify_item():
    pass


def ask_display_all_items():
    pass


def ask_display_item_details():
    pass
