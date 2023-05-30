def ascii_sequence(s):
    # 将每个字符转换为二进制数
    binary_strings = [bin(ord(c))[2:].zfill(8) for c in s]
    # 生成递增的二进制数数列
    binary_sequence = ["".join(binary_strings[:i+1]) for i in range(len(binary_strings))]
    # 初始化搜索二进制数的起点为字符串开头
    start_index = 0
    # 初始化搜索二进制数的终点为字符串末尾
    end_index = len(s) - 1
    # 查找可以找到的最后一个二进制数
    last_binary = ""
    while True:
        found = False
        for i in range(len(binary_sequence)):
            if binary_sequence[i] in s[start_index:]:
                start_index = s.index(binary_sequence[i], start_index) + len(binary_sequence[i])
                found = True
                last_binary = binary_sequence[i]
                break
        if not found:
            break
        for i in range(len(binary_sequence)-1, -1, -1):
            if binary_sequence[i] in s[:end_index+1]:
                end_index = s.rindex(binary_sequence[i], 0, end_index) - 1
                found = True
                last_binary = binary_sequence[i]
                break
        if not found:
            break
        s = s[:start_index-len(last_binary)] + s[start_index:]
        s = s[:end_index+len(last_binary)+1] + s[end_index+1:]
    # 如果不能找到任何二进制数，则返回-1
    if last_binary == "":
        return -1
    # 将字符串转换为八进制数，并递归地应用相同的过程
    octal = oct(int(s, 2))[2:]
    if octal.startswith('0'):
        octal = octal[1:]
    return ascii_sequence(octal)





def main():
    a = input()
    print(ascii_sequence(a))


main()