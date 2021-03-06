class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}, {self.description}"

    def __repr__(self):
        return f"Name: {self.name}, Description: {self.description}"

    def on_take(self):
        print(f"You picked up the {self.name.lower()}")

    def on_drop(self):
        print(f"You dropped the {self.name.lower()}")