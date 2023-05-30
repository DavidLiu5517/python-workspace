a = eval(input("Entry a number: "))
b = eval(input("Entry a number: "))
'''
max = 1
if a < b:
    a,b = b,a
for i in range(1,b+1,1):
    if a % i == 0 and b % i ==0 and i > max:
        max = i
print("the GCD of these two number is ", max)'''
if a < b:
    a,b = b,a
while a % b != 0:
    reminder = a % b
    a = b
    b = reminder
print("the GCD of these two number is ", b)