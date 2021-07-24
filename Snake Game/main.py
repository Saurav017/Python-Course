
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

# set canvas
screen.setup(width=600, height=500)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer()
# It will turn turtle animation on/off

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
#     update the screen at once
    time.sleep(0.02)
    # sleep the screen for 0.1s after every screen update
    snake.move()

    #Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 270 or snake.head.xcor() < -280 or snake.head.ycor() > 220 or snake.head.ycor() < -230:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment) < 10:
            # if head collides with any other segment in tail, then game over
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()