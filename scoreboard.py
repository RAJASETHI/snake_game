from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.goto(0,270)
        self.hideturtle()
        self.printScore()

    def printScore(self):
        self.clear()
        self.write(f"Score:{self.score}", False, "center", font=("Comic Sans MS", 20, "normal"))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write("GAME OVER", False, "center", font=("Comic Sans MS", 16, "normal"))

    def increment(self):
        self.score += 1
        self.printScore()
