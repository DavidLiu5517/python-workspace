n = eval(input())
fi = input().split(" ")
se = input().split(" ")
need = 0


count = 0
for i in fi:
    if i == '1':
        a = 0
        tem = 0
        if count % 2 == 0:
            a = 0
        else:
            if se[count] == "1":
                a = 1
        if count == 0:
            if fi[1] == "1":
                tem += 1
        elif count == n - 1:
            if fi[count -1] == "1":
                tem += 1
        else:
            if fi[count + 1] == "1":
                tem += 1
            if fi[count -1] == "1":
                tem += 1
        need = need + 3 - a - tem
    count += 1



count = 0
for i in se:
    if i == "1":
        a = 0
        tem = 0
        if count % 2 == 0:
            a = 0
        else:
            if fi[count] == "1":
                a = 1
        if count == 0:
            if se[1] == "1":
                tem += 1
        elif count == n - 1:
            if se[count - 1] == "1":
                tem += 1
        else:
            if se[count + 1] == "1":
                tem += 1
            if se[count -1] == "1":
                tem += 1
        need = need + 3 - a - tem
    count += 1    
print(need)