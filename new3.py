import turtle as t
import time
import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


food = t.Turtle()
screen = t.Screen()

screen.tracer(0.1)
class Snake:
    x = 0
    y = 0
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.create_food()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_turtle = t.Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(position)
            self.segments.append(new_turtle)
    def create_food(self):
        food.shape("circle")
        food.color("green")
        food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        food.penup()

    def move(self):
        for snake_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake_num - 1].xcor()
            new_y = self.segments[snake_num - 1].ycor()
            self.segments[snake_num].goto(new_x, new_y)
        self.head.fd(20)
    def increment(self):

        new_turtle = t.Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(self.segments[2].pos())
        self.segments.append(new_turtle)
        screen.update()

    def food_gen(self):
        x_new = random.randint(-255, 255)
        y_new = random.randint(-255, 255)

        food.goto(x=x_new, y=y_new)

    def up(self):
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
