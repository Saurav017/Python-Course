from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    def add_segment(self,positions):
        # to setup our snake of 3 boxes of 20*20
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.speed("fastest")
        new_segment.goto(positions)
        self.all_segments.append(new_segment)

    def extend_snake(self):
        # adding segment to last position
        self.add_segment(self.all_segments[-1].position())

    def move(self):
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            # loop through the segments from last
            new_x = self.all_segments[seg_num - 1].xcor()
            new_y = self.all_segments[seg_num - 1].ycor()
            # Getting the hold of second last segment's coordinates

            self.all_segments[seg_num].goto(new_x, new_y)
            # Moving the last segment to second last segment

        self.all_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        # for not moving his head backward
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

