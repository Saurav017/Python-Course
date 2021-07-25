from turtle import Turtle

class Ball(Turtle):
    # class to create a Ball

    def __init__(self):
        super().__init__()
        # Ball subclass inheriting properties from Turtle class

        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.move_x = 10
        self.move_y = 10
            # move the ball by 10 units

        self.move_speed = 0.1

    def move_ball(self):
        # Method to move the ball

        new_X = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
            # changing the x and y coordinate of the ball
        self.goto(new_X, new_y)


    def bounce_y(self):
        # method to make the ball bounce when it will hit the ball. What it will do is change the direction of y

        self.move_y *= -1


    def bounce_x(self):
        # method to make the ball bounce when it will hit the paddle. What it will do is change the direction of x

        self.move_x *= -1
        self.move_speed *= 0.9

    def reset_the_ball(self):

        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()