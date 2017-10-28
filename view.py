text_colors = {
               'white': '\033[0m',
               'red': '\033[31m',
               'green': '\033[32m'
               }


def get_separate_bar():
    bar_lenght = 60
    separate_bar = bar_lenght * '-'
    return separate_bar


def set_heading_for_display():
    display = []
    separate_bar = get_separate_bar()
    display.append(separate_bar)

    heading = '{0:{algin}{width}}|{1:{algin}{width}}|{2:{algin}{width}}'.format('INDEX', 'NAME', 'STATUS', algin='^', width=20)
    display.append(heading)
    display.append(separate_bar)
    return display


def get_status_of_task(task):
    if task.is_done:
        return text_colors['green'] + 'DONE' + text_colors['white']
    else:
        return text_colors['red'] + 'UNDONE' + text_colors['white']


'''
Functions responsible for displaying all items
'''


def display_table_of_all_items(tasks_archive):
    table_to_display = '\n'.join(prepare_items_to_display(tasks_archive))
    print(table_to_display)


def prepare_items_to_display(tasks_archive):
    display = set_heading_for_display()
    iterate_through_tasks(display, tasks_archive)
    return display


def iterate_through_tasks(display, tasks_archive):
    separate_bar = get_separate_bar()
    tasks = tasks_archive.todo_archive
    for item in tasks:
        index = tasks.index(item)
        name = item.name
        status = get_status_of_task(item)

        data_of_item = '{0:{algin}{width}}|{1:{algin}{width}}|{2:{algin}{width}}'.format(
                                                                                        index, name, status, algin='^', width=20)
        appending_data_to_display(display, data_of_item, separate_bar)


def appending_data_to_display(display, data, separate_bar):
    display.append(data)
    display.append(separate_bar)


'''
Functions responsible for displaying one item's details
'''


def display_item_details(task, index):
    display = set_heading_for_display()
    name = task.name
    status = get_status_of_task(task)
    description = task.description
    appending_details_of_item(display, index, name, status, description)
    details_to_display = '\n'.join(display)
    print(details_to_display)


def appending_details_of_item(display, index, name, status, description):
    separate_bar = get_separate_bar()
    data_of_item = '{0:{algin}{width}}|{1:{algin}{width}}|{2:{algin}{width}}'.format(index, name, status, algin='^', width=20)
    display.append(data_of_item)
    display.append(separate_bar)
    display.append('DESCRIPTION')
    display.append(description)
    display.append(separate_bar)
