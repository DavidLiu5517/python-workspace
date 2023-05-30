def main():
    n = eval(input())
    fi = input().split(" ")
    se = input().split(" ")
    need = 0
    count = 0
    for i in fi:
        if i == '1':
            a = checkSe(1, se, count, n)
            b = checkFi(1, fi, count, n)
            need = need + 3 - a - b
        count += 1
    count = 0
    for i in se:
        if i == "1":
            a = checkSe(2, se, count, n)
            b = checkFi(2, fi, count, n)
            need = need + 3 - a - b
        count += 1    
    print(need)


def checkSe(a, b, c, d):
    if a == 1:
        if c % 2 == 1:
            return 0
        else:
            if b[c] == "1":
                return 1
            else:
                return 0
    else:
        tem = 0
        if c == 0:
            if b[c + 1] == "1":
                tem += 1
        elif c == d - 1:
            if b[c - 1] == "1":
                tem += 1
        else:
            if b[c + 1] == "1":
                tem += 1
            if b[c - 1] == "1":
                tem += 1
        return tem


def checkFi(a, b, c, d):
    if a == 1:
        tem = 0
        if c == 0:
            if b[c + 1] == "1":
                tem += 1
            return tem
        if c == d - 1:
            if b[c - 1] == "1":
                tem += 1
            return tem
        else:
            if b[c + 1] == "1":
                tem += 1
            if b[c - 1] == "1":
                tem += 1
            return tem
    else:
        eo = c % 2
        if eo == 1:
            return 0
        else:
            if b[c] == "1":
                return 1
            else:
                return 0
            


main()