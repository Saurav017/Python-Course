from turtle import Turtle, Screen
import random

colors = ["red", "orange", "blue", "green", "purple", "yellow"]

screen = Screen()

# Setting up a screen for the race
screen.setup(width=500, height=400)

is_race_on = False

# taking the input for the bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the colour.")
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
y_coordinates = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")

    # Placing out turtle to out starting position

    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-238, y=y_coordinates[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        # check for the finish line
        if turtles.xcor() > 230:
            is_race_on = False
            winning_color = turtles.pencolor()

            # Check the bet is correct or not
            if winning_color == user_bet:
                print(f"You Won !! The {winning_color} turtle is the winner.")
            else:
                print(f"You Lose !! The {winning_color} turtle is the winner.")

        # moving the turtles forward at random distance
        rand_distance = random.randint(0, 10)
        turtles.forward(rand_distance)




screen.exitonclick()