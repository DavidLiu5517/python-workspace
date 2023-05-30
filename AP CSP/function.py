def verify(n):
    if not 13 <= len(n) <= 16:
        return "invalid"
    result1 = 0
    for i in n[::2]:
        result1 += int(i) * 2 if int(i) * 2 < 10 else 1 + int(str(int(i) * 2)[1])
    for i in n[1::2]:
        result1 += int(i)
    if result1 % 10 == 0:
        return "valid"
    else:
        return "invalid"
n = input("Entry number of the card: ")
print(verify(n))