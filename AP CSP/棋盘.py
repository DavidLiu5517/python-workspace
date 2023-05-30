import turtle
turtle.speed(0)
length = 20
start = [-4*length, 4*length]
for i in range(1,9):
    for j in range(1,9):
        if (i+j)%2==0:
            turtle.fillcolor("white")
        else:
            turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(start[0], start[1])
        turtle.pendown()
        for c in range(4):
            turtle.right(90)
            turtle.forward(length)
        turtle.end_fill()
        start[0] = start[0]+length
    start[1] = start[1]-length
    start[0] = -4*length
turtle.exitonclick()