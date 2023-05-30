def decimalToBinary(value):
    re = ""
    if value == 0:
        return "0"
    else:
        while value != 0:
            a = value % 2
            value //= 2
            re += str(a)
        re = re[::-1]
        return re

x = eval(input("Entry a number: "))
print(decimalToBinary(x))