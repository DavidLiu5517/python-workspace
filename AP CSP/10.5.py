x = input("Enter ten numbers: ")
inPut = x.split()
list1 = [eval(x) for x in inPut]
list2 = []
for num in list1:
    if num not in list2:
        list2.append(num)
print("The distinct numbers are: ", end="")
for num in list2:
    print(num, end=" ")