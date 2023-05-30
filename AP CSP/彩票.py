test = [range(1, 100)]
while True:
    x = input("enter your numbers with space")
    if x == "0" :
        break
    inpu = [x.split()]
    for i in range(0, len(inpu), 1):
        if inpu[i] in test:
            test.remove(inpu[i])
if len(test) == 0:
    print("covered")
else:
    print("not covered")