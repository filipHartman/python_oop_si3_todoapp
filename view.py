def display_table_of_all_items(tasks):
    table_to_display = '/n'.join(prepare_items_to_display(tasks))
    print(table_to_display)


def get_separate_bar():
    bar_lenght = 40
    separate_bar = 40 * '-'
    return separate_bar


def prepare_items_to_display(tasks):
    display = set_heading_for_display()
    iterate_through_tasks(display, tasks)
    return display


def set_heading_for_display():
    display = []
    separate_bar = get_separate_bar()
    display.append(separate_bar)
    heading = '{0:{algin}{width}}|{1:{algin}{width}}'.format('INDEX', 'NAME', algin='^', width=20)
    display.append(separate_bar)
    return display


def iterate_through_tasks(display, tasks):
    separate_bar = get_separate_bar()
    for item in tasks:
        index = tasks.index(task)
        name = item.name

        data_of_item = '{0:{algin}{width}}|{1:{algin}{width}}'.format(index, name, algin='^', width=20)
        appending_data_to_display(display, data_of_item, separate_bar)


def appending_data_to_display(display, data, second_row, separate_bar):
    display.append(first_row)
    display.append(second_row_of_item)
    display.append(separate_bar)


def display_it
