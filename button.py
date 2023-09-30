class Button:
    def __init__(self, x: int, y: int, title: str):
        self.x = x
        self.y = y
        self.title = title
        self.appearnce = True

    def hide(self):
        self.appearnce = False

    def show(self):
        self.appearnce = True

    def print_status(self):
        print(f"Дані про віджет\n)