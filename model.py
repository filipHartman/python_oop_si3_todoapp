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
