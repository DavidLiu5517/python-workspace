my_input = str(input())
my_input = my_input.split(" ")
n = int(my_input[0])  # int(input("Enter n: "))
b = int(my_input[1])  # int(input("Enter b: "))
s = my_input[2]  # input("Enter s: ")
start = int("%s" % s, b)


def baseconvert(n_, x):
    a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    b = []
    while 1:
        s_ = n_ // x
        y = n_ % x
        b.append(y)
        if s_ == 0:
            break
        n_ = s_
    b.reverse()
    num = ""
    for i in b:
        num += a[i]
    return num


result_list = []
for i in range(n):
    result_list.append(baseconvert(start, b))
    start += 1
result = ""
for items in result_list:
    result += items
temp = set(result)
temp1 = []
for items in temp:
    temp1.append(result.count(items))
print(max(temp1))