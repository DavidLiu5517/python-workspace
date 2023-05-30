def process_string(s):
    arr1 = []
    arr2 = []
    arr2.append(0)
    for i in range(len(s)):
        index = 0
        while index < len(arr1) and s[i] > arr1[index]:
            index += 1
        arr1.insert(index, s[i])
        if index == 0:
            arr2.append(arr2[0] + 1)
        elif index == len(arr1) - 1:
            arr2.append(arr2[-1] + 1)
        else:
            arr2.append(max(arr2[index - 1], arr2[index]) + 1)
    s1 = ""
    s2 = ""
    for i in range(len(arr1)):
        s1 += arr1[i]
        index = arr1.index(arr1[i])
        if index == len(arr1) - 1:
            next_index = -1
        else:
            next_index = arr2.index(arr2[index + 1])
        if index == 0:
            prev_index = -1
        else:
            prev_index = arr2.index(arr2[index - 1])
        for j in range(prev_index + 1, next_index):
            if arr1[j] not in s2:
                s2 += arr1[j]
    return s1 + " " + s2

s=input()
print(process_string(s))