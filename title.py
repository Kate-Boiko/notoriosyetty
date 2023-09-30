class Title:
    def __init__(self, title, x, y):
        self.title = title
        self.x = x
        self.y = y
        self.apperance = False
    
    def hide(self):
        self.apperance = False

    def show(self):
        self.apperance = True

    def print_status(self):
        print(f"Дані про віджет\n{self.title}{self.x}{self.y}{self.apperance}")
              
main_title = Title(150, 50, "Дізнайтсь переможця можно прямо зараз!")
rules_title = Title(150, 50, "Переможець може бути тільки один!")
main_title.print_status()
rules_title.print_status()
rules_title.hide()