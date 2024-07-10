from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, -180)
        self.move_x = 10
        self.move_y = 10
        self.moving_speed = 0.072

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1

    def reset_ball(self):
        self.goto(0, -180)
        self.bounce_y()
        self.moving_speed = 0.072

    def increase_speed(self):
        self.moving_speed *= 0.985

    def game_over(self):
        self.moving_speed = 0
        self.goto(2000, 2000)