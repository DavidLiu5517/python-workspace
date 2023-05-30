def format(num, wid):
    di = 1
    tem = num
    while tem > 10:
        di += 1
        tem //= 10
    a = []
    for i in range(di):
        a.append(num % 10)
        num //= 10
    li = []
    count = 1
    for i in range(di -1, -1, -1):
        li.insert(di - count, a[i])
    if wid <= di:
        re = ''
        for i in li:
            re += str(i)
    else:
        t = wid - di
        re = ''
        for i in range(t):
            re += str(0)
        for i in li:
            re += str(i)
    return re

num = eval(input("Entry an integer: "))
wid = eval(input('Entry the width: '))
print(f"The formatted number is {format(num, wid)}")