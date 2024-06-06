import turtle
from turtle import *


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")

        self.hideturtle()
        self.penup()



    def show(self):
        self.goto(0, 265)
        self.write(f" score {self.score}", align="center", font=("arial", 24, "normal"))




