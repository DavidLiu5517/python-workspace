import random as r
for i in range(4):
    num = r.randint(0,12)
    p = " "
    if num == 0:
        p += "Ace"
    elif num == 10:
        p += "Jack"
    elif num == 11:
        p += 'Queen'
    elif num == 12:
        p += 'King'
    else:
        p += str(num + 1)
    e = r.randint(0,3)
    if e == 0:
        print('Spades',end=p)
    elif e == 1:
        print('Hearts',end=p)
    elif e == 2:
        print('Diamonds',end=p)
    else:
        print('Clubs',end=p)