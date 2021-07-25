from turtle import Turtle

class Paddle(Turtle):

    # class to make a paddle
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        # method to move paddle up

        new_y = self.ycor() + 20
        self.goto(self.xcor(), y=new_y)

    def down(self):
        # method to move paddle down

        new_y = self.ycor() - 20
        self.goto(self.xcor(), y=new_y)

