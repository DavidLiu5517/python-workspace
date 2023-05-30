from random import randint


r = randint(10,99)
g = eval(input("guess this two digit number"))
if g == r:
    print("congratulation you get it, the award is $10,000")
elif g % 10 * 10 + g // 10 == r:
    print("Your input match uop with all the digits, the award is $3,000")
elif g % 10 == r % 10 or g // 10 == r // 10 or g % 10 == r // 10 or g // 10 == r % 10:
    print("one digit is match, the award is $1,000")
else:
    print("You didn't get the number")