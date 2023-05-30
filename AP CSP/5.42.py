#(a)
import random as r
a1 = 50 * 100 / (100 *100)
a3 = 50 * 50 * 0.5 / (100 * 100)
odd = 0
for i in range(1000000):
    a = r.randint(0, 100)
    if a / 100 <= a1:
        odd += 1
    elif a / 100 <= a1 + a3:
        odd += 1
odd = odd / 1000000
print ("The probability of the square fall into a odd-number region is " + str(odd))

'''
(b)
odd = 0
t = eval(input("Entry the time you want to simulate: "))
for i in range(t):
    a = r.randint(0, 100)
    if a / 100 <= a1:
        odd += 1
    elif a / 100 <= a1 + a3:
        odd += 1
print(str(odd) + " times out of " + str(t) + " the square fall into the odd-number region")
'''