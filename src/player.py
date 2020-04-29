class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom

    def __str__(self):
        return f"{self.name}, {self.currentRoom}"

    def __repr__(self):
        return f"Name: {self.name}, Current Room: {self.currentRoom}"