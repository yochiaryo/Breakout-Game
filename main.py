from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from hearts import Hearts
import time


# --- VARIABLES ---
paddle_small = False
WIDTH = 800
HEIGHT = 600
score = 0
spacing_x = WIDTH // 12
height_2 = HEIGHT // 2
hearts_go = 3
incr_speed = 0


# --- LISTS/DICTIONARIES ---
colors = ["red", "red", "orange", "orange", "green", "green", "yellow", "yellow"]
coordinates = [-360, -295, -230, -165, -100, -35, 30, 95, 160, 225, 290, 355]
bricks = []
brick_values = {
    "red": 7,
    "orange": 5,
    "green": 3,
    "yellow": 1,
}
brick_speed_values = {
    "red": 0.985,
    "orange": 0.985,
}


# --- SCREEN ---
screen = Screen()
screen.bgcolor("black")
screen.setup(WIDTH, HEIGHT)
screen.title("Breakout Game")
screen.tracer(0)

# --- OBJECTS ---
paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()
hearts = Hearts()


# --- BRICKS ---
for item in range(0, 8):
    new_height = height_2 - 60
    for i, color in enumerate(coordinates):
        brick = Turtle()
        brick.color(colors[item])
        brick.shape("square")
        brick.shapesize(1, 3)
        brick.penup()
        brick.setpos(-WIDTH // 2 + (i + 0.5) * spacing_x, HEIGHT // 2.2 - (item + 1) * (HEIGHT // 22))
        bricks.append(brick)


# Controlling paddle with left and right keys
screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")


game_is_on = True
while game_is_on:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.move()

    # Detect hit with left and right walls
    if ball.xcor() > 370 or ball.xcor() < -370:
        ball.bounce_x()

    # Detect hit with upper wall
    if ball.ycor() > 280:
        ball.bounce_y()
        ball.increase_speed()
        paddle.shapesize(1, 5)
        paddle_small = True

    # Detect if ball hit the paddle
    # If ball hit the upper wall, the paddle shrinks and the ball won't hit the empty space next to the paddle
    if paddle_small:
        if ball.ycor() < -220 and ball.distance(paddle) < 40:
            ball.bounce_y()
    else:
        if ball.ycor() < -220 and ball.distance(paddle) < 80:
            ball.bounce_y()

    # Detect if ball missed the paddle
    if ball.ycor() < -280:
        ball.reset_ball()
        hearts.lose_heart()
        hearts_go -= 1
        if hearts_go == 0:
            # If user has no hearts left, all the remaining bricks disappear from the game screen
            for bri in bricks:
                bri.goto(-2000, -2000)
            scoreboard.add_game_over()
            ball.game_over()
            paddle.game_over()

    for br in bricks:
        # Detects if the ball hit any bricks
        if ball.distance(br) < 30:
            for (key, value) in brick_values.items():
                # Checks what color brick the ball hit and adds its value to score
                if br.color()[0] == key:
                    score += value
                    scoreboard.increase_score(value)

            for (key, value) in brick_speed_values.items():
                # Checks if the brick hit was orange or red and increases the ball moving speed
                if br.color()[0] == key:
                    ball.moving_speed *= value
            # Every 4 and 12 bricks hit, it increases the ball moving speed
            incr_speed += 1
            if incr_speed % 4 == 0:
                ball.moving_speed *= 0.985
            if incr_speed % 12 == 0:
                ball.moving_speed *= 0.985
            # If the brick gets hit, it goes somewhere out of the main game screen
            ball.bounce_y()
            br.goto(1000, 1000)

    # Detect if all the bricks were hit and shows that the user has won
    if incr_speed == 96:
        scoreboard.add_win()
        paddle.game_over()
        ball.game_over()


screen.exitonclick()
