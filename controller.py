from model import *


def ask_add_item(tasks_archive):
    name = input('Enter the name of task to do: ')
    description = input('Enter the description of task to do: ')
    task = ToDo_item(name, description)
    tasks_archive.todo_archive.append(task)


def ask_delete_item(tasks_archive):
    # here we need to display whole list of tasks
    index = int(input('Enter index number of item to delete: '))
    index -= 1
    tasks_archive.todo_archive.pop(index)


def ask_modify_item(tasks_archive):
    # here we need to display whole list of tasks
    index = int(input('Enter index number of item to modify: '))
    task = tasks_archive.todo_archive[index]
    choice = input('What do you want modify: name (n) or description (d)? ')
    make_modification(choice)


def make_modification(choice):
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
def ask_display_all_items():
    pass


def ask_display_item_details():
    pass
