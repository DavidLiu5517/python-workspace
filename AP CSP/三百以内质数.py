for i in range(1,301,1):
    count = 0
    for a in range(2,i+1,1):
        if i % a == 0:
            count += 1
    if count == 1:
        print(i, end=" ")