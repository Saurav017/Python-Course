from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        # keep track of the scores

        self.update_scoreboard()
    #     update score when the paddle misses

    def update_scoreboard(self):


        self.clear()

        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        # left score

        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))
        # right score


    def l_point(self):

        # update the left side score if right misses
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):

        # update the right side score if left misses
        self.r_score += 1
        self.update_scoreboard()