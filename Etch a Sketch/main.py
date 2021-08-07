from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_clockwise():
    tim.left(10)
    tim.forward(10)

def move_anticlockwise():
    tim.right(10)
    tim.forward(10)

def clear():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_anticlockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
