from turtle import Turtle


class Hearts(Turtle):
    def __init__(self):
        super().__init__()
        self.hearts = "❤️❤️❤️"
        self.display_hearts(self.hearts)

    def display_hearts(self, hearts):
        self.clear()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(-380, 260)
        self.write(f"{hearts}", font=("Calibri", 24, "normal"))

    def lose_heart(self):
        self.hearts = self.hearts[:-2]
        self.display_hearts(self.hearts)
