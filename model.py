class ToDo_item():
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

    def __str__(self):
        pass


class ToDo_archive():

    def __init__(self):
        self.todo_archive = []

    def add_item(self, task):
        self.todo_archive.append(task)

    def delete_item(self, index):
        self.todo_archive.pop(index)
