h = input("please enter a hex character: ")
if h.isalpha():
    if h == 'A':
        print("10")
    elif h == "B":
        print("11")
    elif h == "C":
        print("12")
    elif h == "D":
        print("13")
    elif h == "E":
        print("14")
    elif h == "F":
        print("15")
    else:
        print("Invalid input")
elif h < 10:
    print(h)
else:
    print("Invalid input")