from turtle import Turtle
import random

class Food(Turtle):
    # inheriting Turtle class in Food class

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
            # stretch the circle along its length and width
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        # getting random coordinates of x and y for food from  (-280, 280)
        num_x = random.randint(-250, 250)
        num_y = random.randint(-240, 210)

        self.goto(num_x, num_y)
        # goto random (x,y) location