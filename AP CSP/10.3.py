x = input("Enter integers between 1 and 100: ")
inPut = x.split()
count = 0
lst = [eval(x) for x in inPut]
t = lst
for tem in sorted(lst):
    for te in sorted(t):
        if tem == te:
            count += 1
    if count != 0:
        print(tem, " occurs ", count, " times")
    while count != 0:
        t.remove(tem)
        count -= 1