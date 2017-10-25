class ToDo_archive():

    def __init__(self):
        self.todo_archive = []

    def add_item(self, task):
        self.todo_archive.append(task)

    def delete_item(self, index):
        self.todo_archive.pop(index)
