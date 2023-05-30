pw = input("Entry password: ")
def checkPW(pw):
    count = 0
    if len(pw) >= 8:
        if pw.isalnum():
            for i in range(0,len(pw)):
                if pw[i].isdigit():
                    count += 1
            if count >= 2:
                print("valid password")
    else:
        print("invalid password")
checkPW(pw)