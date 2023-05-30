li = str(input("Entry ten numbers: "))
li = li.split(" ")
for i in li:
    a = i
    for b in range(li.count(a)-1):
        li.remove(a)
x = list(map(int, li))
x.sort()
print("The dis tinct numbers are: ", end="")
for i in x:
    print(i, end="")