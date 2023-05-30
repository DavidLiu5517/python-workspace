import turtle as t
import random as r
w = t.Screen()
lb = -(w.window_width()/2)
rb = w.window_width()/2
tb = w.window_height()/2
bb = -(w.window_height()/2)
while (lb < t.xcor() < rb) and (bb < t.ycor() < tb):
    a = r.randint(1,2)
    if a == 1:
        t.right(90)
    else:
        t.left(90)
    t.forward(50)