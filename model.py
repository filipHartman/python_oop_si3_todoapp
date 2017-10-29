import csv

class TodoItem():
    def __init__(self, name, description, is_done=False):
        self.name = name
        self.description = description
        self.is_done = is_done

    def change_name(self, new_name):
        self.name = new_name

    def change_description(self, new_description):
        self.description = new_description

    def mark_as_done(self):
        self.is_done = True

    def get_status(self):
        if self.is_done:
            return 'DONE'
        else:
            return 'UNDONE'


class TodoArchive():

    def __init__(self):
        self.todo_archive = []

    def add_item(self, task):
        self.todo_archive.append(task)

    def delete_item(self, task):
        self.todo_archive.remove(task)

    def export_tasks(self):

        tasks_to_save = []

        for task in self.todo_archive:
            tasks_to_save.append([task.name, task.description, task.get_status()])

        with open('tasks.txt', 'w') as tasks_file:
            tasks_csv = csv.writer(tasks_file, delimiter='|')
            tasks_csv.writerows(tasks_to_save)

    def import_tasks(self):
        with open('tasks.txt', 'r') as tasks_file:
            tasks_csv = csv.reader(tasks_file, delimiter='|')
            file_has_tasks = bool(tasks_csv)

            if file_has_tasks:
                self.fill_todo_archive_from_file(tasks_csv)

    def change_status_to_bool(self, status_str):
        if status_str == 'DONE':
            return True
        elif status_str == 'UNDONE':
            return False

    def fill_todo_archive_from_file(self, tasks_csv):
        name_column = 0
        description_column = 1
        status_column = 2
        for task in tasks_csv:

            name = task[name_column]
            description = task[description_column]
            status_str = task[status_column]
            status = self.change_status_to_bool(status_str)

            todo_item = TodoItem(name, description, status)

            self.add_item(todo_item)
