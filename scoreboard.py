from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.goto(0, 270)
        with open("highestScore.txt", mode="r+") as self.file:
            self.lk = [i for i in self.file.read().split() if i.isdigit()]
        self.highScore = int("".join(self.lk))
        self.highScore = int(self.highScore)
        self.hideturtle()
        self.printScore()
        self.penup()

    def printScore(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.highScore}", False, "center",
                   font=("Comic Sans MS", 20, "normal"))

    # ### High Score is going to be updated
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, "center", font=("Comic Sans MS", 16, "normal"))

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("highestScore.txt", mode="w") as self.file:
                self.file.write(str(self.highScore))

        self.score = 0
        self.printScore()

    def increment(self):
        self.score += 1
        self.printScore()
