class Room:
    def __init__(self, name, description, n_to, e_to, s_to, w_to):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __str__(self):
        return f"{self.name}, {self.description}"

    def __repr__(self):
        return f"Name: {self.name}, Description: {self.description}"