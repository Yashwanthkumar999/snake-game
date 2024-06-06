
import turtle as t
import random
import time

sc = t.Screen()
sc.setup(600, 600)
sc.tracer(0.1)

food = t.Turtle()
food.goto(50,50)
food.penup()
print(food.pos())
food.goto(100,100)
sc.update()
food.goto(-100,100)
sc.update()
colors = ["red", "blue", "green"]
colors.insert(2,"pink")
print(colors)




sc.exitonclick()
