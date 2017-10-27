def display_table_of_all_items(tasks):
    table_to_display = '/n'.join(prepare_items_to_display(tasks))
    print(table_to_display)


def get_separate_bar():
    bar_lenght = 40
    separate_bar = 40 * '-'
    return separate_bar


def prepare_items_to_display(tasks):
    display = []
    iterate_through_tasks(display, tasks)
    return display


def iterate_through_tasks(display, tasks):
    separate_bar = get_separate_bar()
    display.append(separate_bar)
    for item in tasks:
        index = tasks.index(task)
        name = item.name
        description = item.description

        first_row_of_item = 'INDEX: {0}  NAME: {1}'.format(index, name)
        second_row_of_item = 'DESCRIPTION:\n{}'.format(description.upper())
        appending_data_to_display(display, first_row_of_item, second_row_of_item, separate_bar)


def appending_data_to_display(display, first_row, second_row, separate_bar):
    display.append(first_row)
    display.append(second_row_of_item)
    display.append(separate_bar)
