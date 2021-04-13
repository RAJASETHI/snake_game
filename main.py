from turtle import Turtle, Screen, listen, onclick
import time

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snaky_Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
# screen.update()
is_move = True

while is_move:
    screen.update()
    time.sleep(0.1)
    # snake.move()

    # Collision with Food
    if snake.head.distance(food) < 20:
        scoreboard.increment()
        food.colide()
        snake.extend()

    # Collision with Wall
    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() <= -290 or snake.head.ycor() >= 290:
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
    # Collision with the tail

    for i in snake.snake[1:]:

        if snake.head.distance(i) < 5:
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()
            # break
    snake.move()
screen.exitonclick()
