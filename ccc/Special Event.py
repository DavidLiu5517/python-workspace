n = eval(input())
a = []
for i in range(n):
    tem = input()
    b = []
    for i in range(5):
        b.append(tem[i])
    a.append(b)
d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0
for i in a:
    count = 1
    for t in i:
        if t == 'Y':
            if count == 1:
                d1 += 1
            elif count == 2:
                d2 += 1
            elif count == 3:
                d3 += 1
            elif count == 4:
                d4 += 1
            else:
                d5 += 1
        count += 1
d1 = n -d1
d2 = n -d2
d3 = n -d3
d4 = n -d4
d5 = n -d5
d = [d1,d2,d3,d4,d5]
o = ''
te = 0
blo = True
while te <= 5:
    for i in d:
        if i == te:
          blo = False
    if not blo:
        break  
    te += 1
if d1 == te:
    o += '1'
if d2 == te:
    if o == '':
        o += '2'
    else:
        o += ',2'
if d3 == te:
    if o == '':
        o += '3'
    else:
        o += ',3'
if d4 == te:
    if o == '':
        o += '4'
    else:
        o += ',4'
if d5 == te:
    if o == '':
        o += '5'
    else:
        o += ',5'
print(o)