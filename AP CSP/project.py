def Main():
    userInput={"increasing speed of the net profit(in %): ":0,"net profit: ":0,"P/E ratio(in number): ":0,"increasing speed of the net profit of last year(in %): ":0}
    for key in userInput:
        userInput[key] = float(input("Please enter " + key ))
    com = input("Please chose the type of company from Internet Industry, Traditional Industry, and Emerging Company. ")
    inter(com, userInput)
    return


def inter(com = '', userIn = {}):
    userInput = list(userIn.values())
    while com != 'Internet Industry' and com != 'Traditional Industry' and com != 'Emerging Company':
        com = input('Please input the correct type of company.')
    if com == 'Emerging Company':
        emergingCompany(userInput[0], userInput[1], userInput[2], userInput[3])
    elif com == 'Traditional Industry':
        traditionalIndustry(userInput[0], userInput[1], userInput[2], userInput[3])
    elif com == 'Internet Industry':
        internetIndustry(userInput[0], userInput[1], userInput[2], userInput[3])
    return

def internetIndustry(speed = 0.0, net = 0.0, pe = 0.0, spe = 0.0):
    score = 0
    if speed < 0 and net < 0:
        print('This is not a good company to invest in whatever the price is since the net profit and the increasing speed for this company are less than 0.')
        return
    if speed > 0 and net < 0:
        print("It is hard to give an answer, you need to see how big the company is, how many monthly active users they have, and how easy they can get replaced.")
        return
    if speed > 0 and net >= 0:
        if pe > 30:
            score -= (pe - 30) * 0.3
        else:
            score += (30 - pe) * 0.3
        if spe < speed:
            score += (speed - spe) * 2
        if speed > 10:
            score += speed * 2
        elif speed > 5:
            score += speed * 1.5
        else:
            score += speed
        if score > 20:
            print("This company's price and their ability on making profit is worth to invest.")
        elif score >0:
            print("This company's price and their ability on making profit is ok to invest, but still need deeper look at their operation part.")
        else:
            print("This company's price and their ability on making profit is not worth to invest, but if the price goes down whiel other maintenance the same it is ok to invest.")
        return
    if speed < 0 and net >= 0:
        if pe > 30:
            score -= (pe - 40) * 0.3
        else:
            score += (40 - pe) * 0.3
        if spe > speed:
            score -= (speed - spe) * 2
        if speed > -5:
            score -= speed
        elif speed > -10:
            score -= speed * 1.5
        else:
            score -= speed * 2
        if score > 20:
            print("This company's price and their ability on making profit is worth to invest.")
        elif score >0:
            print("This company's price and their ability on making profit is ok to invest, but still need deeper look at their operation part.")
        else:
            print("This company's price and their ability on making profit is not worth to invest.")
        return
        




        

def traditionalIndustry(speed = 0.0, net = 0.0, pe = 0.0, spe = 0.0):
    score = 0
    if speed < 0 and net < 0:
        print('This is not a good company to invest in whatever the price is since the net profit and the increasing speed for this company are less than 0.')
        return
    if speed > 0 and net < 0:
        print("It is hard to give an answer, you need to see how big the company is, how many monthly active users they have, and how easy they can get replaced.")
        return
    if speed > 0 and net >= 0:
        if pe > 30:
            score -= (pe - 30) * 0.7
        else:
            score += (30 - pe) * 0.7
        if spe < speed:
            score += (speed - spe) * 1.5
        if speed > 10:
            score += speed * 1.5
        elif speed > 5:
            score += speed * 1.3
        else:
            score += speed
        if score > 20:
            print("This company's price and their ability on making profit is worth to invest.")
        elif score >0:
            print("This company's price and their ability on making profit is ok to invest, but still need deeper look at their operation part.")
        else:
            print("This company's price and their ability on making profit is not worth to invest, but if the price goes down whiel other maintenance the same it is ok to invest.")
        return
    if speed < 0 and net >= 0:
        if pe > 30:
            score -= (pe - 30) * 0.7
        else:
            score += (30 - pe) * 0.7
        if spe > speed:
            score -= (speed - spe) * 1.5
        if speed > -5:
            score -= speed
        elif speed > -10:
            score -= speed * 1.3
        else:
            score -= speed * 1.5
        if score > 30:
            print("This company's price and their ability on making profit is worth to invest.")
        elif score >0:
            print("This company's price and their ability on making profit is ok to invest, but still need deeper look at their operation part.")
        else:
            print("This company's price and their ability on making profit is not worth to invest.")
        return

def emergingCompany(speed = 0.0, net = 0.0, pe = 0.0, spe = 0.0):
    score = 0
    if speed < 0 and net < 0:
        print('This is not a good company to invest in whatever the price is since the net profit and the increasing speed for this company are less than 0.')
        return
    if speed > 0 and net < 0:
        print("It is hard to give an answer, you need to see how big the company is, how many monthly active users they have, and how easy they can get replaced.")
        return
    if speed > 0 and net >= 0:
        if pe > 30:
            score -= (pe - 30) * 0.5
        else:
            score += (30 - pe) * 0.5
        if spe < speed:
            score += (speed - spe) * 1.7
        if speed > 10:
            score += speed * 1.7
        elif speed > 5:
            score += speed * 1.2
        else:
            score += speed
        if score > 20:
            print("This company's price and their ability on making profit is worth to invest.")
        elif score >0:
            print("This company's price and their ability on making profit is ok to invest, but still need deeper look at their operation part.")
        else:
            print("This company's price and their ability on making profit is not worth to invest, but if the price goes down whiel other maintenance the same it is ok to invest.")
        return
    if speed < 0 and net >= 0:
        if pe > 30:
            score - (pe - 30) * 0.5
        else:
            score + (30 - pe) * 0.5
        if spe > speed:
            score - (speed - spe) * 1.7
        if speed > -5:
            score -= speed
        elif speed > -10:
            score -= speed * 1.2
        else:
            score -= speed * 1.7
        if score > 20:
            print("This company's price and their ability on making profit is worth to invest.")
        elif score >0:
            print("This company's price and their ability on making profit is ok to invest, but still need deeper look at their operation part.")
        else:
            print("This company's price and their ability on making profit is not worth to invest.")
        return

Main()
pan = True
while pan:
    print("Do you want to check another company? (Y/N)")
    answer = input()
    if answer == 'Y':
        Main()
    elif answer == 'N':
        pan = False
    else:
        print("Please enter Y or N.")
print("Thank you for using this program, have a nice day!")
print("Thank you for using this program, have a nice day!")