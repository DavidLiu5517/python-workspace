p = eval(input("enter a number"))
for i in range (p):
    for g in range (1,p-i):
        print(" ", end = " ")
    for a in range (i+1, 0,-1):
        print(a, end = " ")
    for x in range (2, i+2):
        print(x, end = " ")
    print()