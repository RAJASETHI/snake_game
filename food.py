from turtle import Turtle
import random as rd


class Food(Turtle):
    def __init__(self):
        super().__init__()
        # self.food = Turtle()
        self.shape("turtle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.colide()

    def colide(self):
        posx = rd.randint(-270, 270)
        posy = rd.randint(-270, 270)
        self.goto(posx,posy)
