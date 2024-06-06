from new3 import *
import turtle as t
from scoreboard import ScoreBoard
import random

sc = t.Screen()
sc.setup(600, 600)
sc.bgcolor("black")
sc.title("snake game")

sc.tracer(0)

board = ScoreBoard()
board.show()

snake = Snake()
snake.food_gen()

sc.listen()

sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")


food_position = (food.xcor(), food.ycor())
race_on = True
while race_on:
    sc.update()
    time.sleep(0.1)

    snake.move()

    if snake.segments[0].distance(food.pos()) <= 15:
        snake.food_gen()
        snake.increment()
    sc.update()


sc.exitonclick()
