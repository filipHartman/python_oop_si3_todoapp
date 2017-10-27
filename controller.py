from model import *
from view import *


def ask_add_item(tasks_archive):
    name = input('Enter the name of task to do: ')
    description = input('Enter the description of task to do: ')
    task = ToDo_item(name, description)
    tasks_archive.todo_archive.append(task)


def get_item_by_index(tasks_archive):
    display_all_items(tasks_archive)
    index = int(input('Enter index of item: '))
    task = tasks_archive.todo_archive[index]
    return task


def ask_delete_item(tasks_archive):
    print('DELETING ITEM FROM ARCHIVE\n')
    display_all_items(tasks_archive)
    # here we need to display whole list of tasks
    task = get_item_by_index(tasks_archive)
    tasks_archive.todo_archive.remove(task)


def ask_modify_item(tasks_archive):
    print('MODIFYING ITEM\'S PARAMETERS\n')

    task = get_item_by_index(tasks_archive)
    choice = input('What do you want modify: name (n) or description (d)? ')
    make_modification(task, choice)


def make_modification(task, choice):
    if choice in ['n', 'name']:
        new_name = input('Enter the new name for choosen task: ')
        task.change_name(new_name)

    elif choice in ['d', 'description']:
        new_description = input('Enter the new description of choosen task: ')
        task.change_description(new_description)
    else:
        pass
    """
    ZABEZPIECZ TO!!!!!!!!!!!!!!!!!!!!!!!!!
    """


def display_all_items(tasks_archive):
    tasks_to_display = tasks_archive.todo_archive
    display_table_of_all_items(tasks_archive)


def display_item(tasks_archive):
    display_all_items(tasks_archive)
    task = get_item_by_index(tasks_archive)
    index = tasks_archive.index(task)
    display_item_details(task, index)
