from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")

class Scoreboard(Turtle):
    # class to keep track of score board

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 210)
        self.update_scoreboard()

    def update_scoreboard(self):
        # update the score board
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
    #     printing game over when the snake hit the wall
        self.goto(0, 0)
        self.write("Game Over!!", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        # method to increase a score
        self.score += 1
        self.clear()
        #     clear() is clear the previous text that was written in the scoreboard
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))