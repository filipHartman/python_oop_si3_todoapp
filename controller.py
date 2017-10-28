from model import *
from view import *
import os
'''
MAIN FUNCTIONS
'''


def create_tasks_archive():
    tasks_archive = TodoArchive()
    return tasks_archive


def ask_add_item(tasks_archive):
    print('-----> ADDITION NEW ITEM TO ARCHIVE <-----\n')
    name = input('Enter the name of task to do: ')
    description = input('\nEnter the description of task to do: ')
    task = TodoItem(name, description)
    tasks_archive.add_item(task)


def ask_delete_item(tasks_archive):
    print('-----> DELETING ITEM FROM ARCHIVE <-----\n')
    task = get_item_by_index(tasks_archive)
    tasks_archive.delete_item(task)


def ask_modify_item(tasks_archive):
    print('-----> MODIFYING ITEM\'S PARAMETERS <-----\n')

    task = get_item_by_index(tasks_archive)
    choice = input('What do you want modify: name (n) or description (d)? ')
    make_modification(task, choice)


def mark_selected_item(tasks_archive):
    print('-----> MARK ITEM AS DONE <-----\n')
    task = get_item_by_index(tasks_archive)
    task.mark_as_done()
    print('Status of task has been changed to \'DONE\'\n')


def display_all_items(tasks_archive):
    if check_tasks_archive_is_empty(tasks_archive):
        print('-----> Tasks archive is empty <-----.\n')
    else:
        display_table_of_all_items(tasks_archive)


def display_item(tasks_archive):
    if check_tasks_archive_is_empty(tasks_archive):
        print('-----> Tasks archive is empty <-----.\n')
    else:
        task = get_item_by_index(tasks_archive)
        os.system('clear')
        index = tasks_archive.todo_archive.index(task)
        display_item_details(task, index)


def export_tasks_to_file(tasks_archive):
    tasks_archive.export_tasks()
    print('\n-----> Tasks have been exported to file. <-----\n')


'''
SUPPORTING FUNCTIONS
'''


def get_item_by_index(tasks_archive):
    display_all_items(tasks_archive)
    index = int(input('Enter index of item: '))
    task = tasks_archive.todo_archive[index]
    return task


def make_modification(task, choice):
    os.system('clear')

    if choice in ['n', 'name']:
        new_name = input('Enter the new name for choosen task: ')
        task.change_name(new_name)
        print('\nName has been changed.\n')
    elif choice in ['d', 'description']:
        new_description = input('Enter the new description of choosen task: ')
        task.change_description(new_description)
        print('\nDescription has been changed.\n')


def check_tasks_archive_is_empty(tasks_archive):
    if tasks_archive.todo_archive == []:
        return True
    return False
