from itertools import count
import math
import turtle
turtle.speed(0)
turtle.Screen()
for i in range(721):
    y = math.sin(math.radians(i))
    turtle.goto(i , y * 100)
turtle.exitonclick()