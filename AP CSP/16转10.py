def hexad(he):
    size = len(he) - 1
    re = 0
    for i in he[::1]:
        if i.isdigit():
            tem = int(i)
        else:
            tem = ord(i) - 87
        re += 16**size * tem
        size -= 1
    return re

he = input("Enter a hexadecimal number: ")
print(hexad(he))