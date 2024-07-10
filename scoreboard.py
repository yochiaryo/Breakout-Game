from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.score_new()

    def score_new(self):
        self.clear()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(240, 260)
        self.write(f"Score: {self.score}", font=("Calibri", 24, "normal"))

    def increase_score(self, brick_score):
        self.score += brick_score
        self.score_new()

    def add_game_over(self):
        self.clear()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-150, 0)
        self.write("Game Over", font=("Calibri", 50, "normal"))

    def add_win(self):
        self.clear()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-100, 0)
        self.write("You won!", font=("Calibri", 50, "normal"))
        self.goto(-100, -50)
        self.write(f"Final Score: {self.score}", font=("Calibri", 30, "normal"))


