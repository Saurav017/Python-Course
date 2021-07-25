
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong ")
screen.tracer(0)
# It will turn turtle animation on/off

screen.listen()

# movement of our right paddle
screen.onkey(key="Up", fun=l_paddle.up)
screen.onkey(key="Down", fun=l_paddle.down)

#movement of our left paddle
screen.onkey(key="w", fun=r_paddle.up)
screen.onkey(key="s", fun=r_paddle.down)


is_game_on = True

while is_game_on:

    time.sleep(ball.move_speed)
    # sleep the screen for 0.1s

    screen.update()
    # update the screen at once

    ball.move_ball()
    # move the ball in while game is on

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
#       if this happens make the ball bounce
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() > 320 or ball.distance(r_paddle) < 50 and ball.xcor() < -320:
        """
        if the ball distance is less than 50 and as the ithe distance is always measured from the center,
        so we have to compare it with cartesian coordinates also. 
        """
        ball.bounce_x()

    # Detecting ball going out of the wall in right side
    if ball.xcor() > 380:
        ball.reset_the_ball()
        scoreboard.l_point()

    # Detecting ball going out of the wall in left side
    if ball.xcor() < -380:
        ball.reset_the_ball()
        scoreboard.r_point()

screen.exitonclick()

