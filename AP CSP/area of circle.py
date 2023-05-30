import math
h = eval(input("please enter your height: "))
if h > 3:
    h = h /100
w = eval(input("please enter your weight: "))
bmi = w / math.pow(h,2)
if bmi > 30:
    print("Obese")
elif bmi > 25:
    print("Overweight")
elif bmi > 18.5:
    print("Normal")
else:   
    print("Underweight")