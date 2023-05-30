inp = input().split(" ")
a = []
for i in inp:
    for j in i[::]:
        a.append(j)
ascii = ""
for i in a:
    ascii = ascii + str(ord(i))
num = 0

pan = True
while pan:
    tem = bin(num)
    if ascii.count(str(tem)) > 0:
        if ascii.count(str(tem)) == 1:
            pl = ascii.find(str(tem))
            ascii = ascii[:pl] + ascii[pl+1:]
        if ascii > 1:
            pl = ascii.rfind(str(tem))
            ascii = ascii[:pl] + ascii[pl+1:]
            pl = ascii.find(str(tem))
            ascii = ascii[:pl] + ascii[pl+1:]
    num += 1
    if ascii.count(str(tem)) == 0:
        pan = False

ascii = str(oct(int(ascii)))
num = 0
pan = True
while pan:
    tem = oct(num)
    if ascii.count(str(tem)) > 0:
        if ascii.count(str(tem)) == 1:
            pl = ascii.find(str(tem))
            ascii = ascii[:pl] + ascii[pl+1:]
        if ascii > 1:
            pl = ascii.rfind(str(tem))
            ascii = ascii[:pl] + ascii[pl+1:]
            pl = ascii.find(str(tem))
            ascii = ascii[:pl] + ascii[pl+1:]
    if ascii.count(str(tem)) == 0:
        print(int(num,8))
        pan = False
    num += 1