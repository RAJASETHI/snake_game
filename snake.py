from turtle import *

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        # for i in range(3):
        #     self.snake.append(Turtle("square"))
        #     self.snake[i].color("yellow")
        #     self.snake[i].penup()
        #     if i > 0:
        #         self.snake[i].goto(self.snake[i - 1].xcor() - 20, 0)
        # self.snake[0].color("medium violet red")
        # self.snake[0].shape("square")
        self.create()
        # register_shape("tenor", "tenor.gif")
        # self.snake[0].shape("tenor")
        self.head = self.snake[0]

    def create(self):
        for i in range(3):
            self.snake.append(Turtle("square"))
            self.snake[i].color("yellow")
            self.snake[i].penup()
            if i > 0:
                self.snake[i].goto(self.snake[i - 1].xcor() - 20, 0)
        self.snake[0].color("medium violet red")
        self.snake[0].shape("square")

    def extend(self):
        self.snake.append(Turtle("square"))
        if len(self.snake) % 4 == 0:
            self.snake[-1].color("green yellow")
        elif len(self.snake) % 9 == 0:
            self.snake[-1].color("gold")
        else:
            self.snake[-1].color("yellow")
        self.snake[-1].penup()
        self.snake[-1].goto(self.snake[-2].xcor(), self.snake[-2].ycor())

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].xcor(), self.snake[i - 1].ycor())
        self.snake[0].forward(MOVE_DISTANCE + 5)

    def up(self):
        if self.head.heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for i in self.snake:
            i.goto(1000, 1000)
        self.snake.clear()
        self.create()
        self.head = self.snake[0]
