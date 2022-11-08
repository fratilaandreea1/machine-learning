class Point:
    def __init__(self, x, y,zona):
        self.x = x
        self.y = y
        self.zona = zona

    def __repr__(self):
        return f"{self.x}, {self.y}, {self.zona} \n"
