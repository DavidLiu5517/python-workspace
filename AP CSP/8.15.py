x = input("Enter the first 9 digits of an ISBN-10 as a string: ")
count = 0
sum = 0
for i in x[::1]:
    count += 1
    sum += int(i) * count
if sum % 11 == 10:
    x += "X"
else:
    x += str(sum % 11)
print("The ISBN-10 number is " + x)