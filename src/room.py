from item import Item

class Room:
    def __init__(self, name, description, items=[], n_to=None, e_to=None, s_to=None, w_to=None):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to

    def __str__(self):
        return f"{self.name}, {self.description}"

    def __repr__(self):
        return f"Name: {self.name}, Description: {self.description}"