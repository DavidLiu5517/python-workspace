count = 1
max = -float('inf')
while True:
    b = eval(input("Entry a number, (0: for the end of the input): "))
    if b == 0:
        break
    if b > max:
        max = b
        count = 1
    elif b == max:
        count += 1

print("The largest number is " + str(max))
print("The occurrence count of the largest number is " + str(count))