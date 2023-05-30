f = eval(input("please enter your first number: "))
s = eval(input("please enter your second number: "))
t = eval(input("please enter your third number: "))
if f >= s >= t:
    print(f , s , t)
elif f >= t >= s:
    print(f , t , s)
elif s >= f >= t:
    print(s , f , t)
elif s >= t >= f:
    print(s , t , f)
elif t >= s >= f:
    print(t , s , f)
elif t >= f >= s:
    print(t , f , s)