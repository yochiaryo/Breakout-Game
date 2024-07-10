from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 8)
        self.color("blue")
        self.penup()
        self.goto(0, -250)

    def go_right(self):
        new_x = self.xcor() + 80
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 80
        self.goto(new_x, self.ycor())

    def game_over(self):
        self.goto(1000, 1000)
