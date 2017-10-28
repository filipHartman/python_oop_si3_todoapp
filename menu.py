menu_commands = ['ADD NEW TASK',
                 'MODIFY TASK',
                 'DELETE TASK',
                 'MARK TASK AS DONE',
                 'SHOW ALL TASKS',
                 'SHOW DETAILS OF SPECIFIC TASK',
                 'EXPORT TASKS TO FILE']


def display_welcome_text():
    print('TO-DO APPLICATION\n')


def display_commands_menu():
    for option in menu_commands:
        print('{} -----> {}'.format((menu_commands.index(option)+1), option))
    print('0 -----> EXIT')
    print('\n')
