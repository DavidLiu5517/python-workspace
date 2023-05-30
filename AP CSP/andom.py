from itertools import count
import math
from re import T
import turtle
import random
n1 = random.randint(0,10)
n2 = random.randint(0,10)
if n1 < n2:
    sw = n1
    n1 = n2
    n2 = sw
n3 = n1 - n2
num = eval(input("What is " + str(n1) + " - " + str(n2) + "?"))
if num == n3:
    print("You are correct!")
else:
    print("Your answer in wrong.")
    print(str(n1) + " - " + str(n2) + " is " + str(n3) + ".")