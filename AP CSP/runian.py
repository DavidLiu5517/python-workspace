y = eval(input("please enter a year: "))
if y % 400 ==0:
    print("It is a leap year")
elif not y % 100 == 0 and y % 4 == 0: 
    print("It is a leap year")
else:
    print("It is not a leap year")