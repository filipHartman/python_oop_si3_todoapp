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
            tasks_to_save.append([task.name, task.description, str(task.is_done)])

        with open('tasks.txt', 'w') as tasks_file:
            tasks_csv = csv.writer(tasks_file)
            tasks_csv.writerows(tasks_to_save)
