def prefix(s1, s2):
    if len(s1 > s2):
        di = len(s2)
    else:
        di = len(s1)
    count = 0
    com = 0
    tem = di
    while count == com & tem >= 0:
        count += 1
        if s1[di - tem] == s2[di - tem]:
            com += 1
            tem -= 1
    if com == 0:
        return ""
    else:
        return s1[:com -1]