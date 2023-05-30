from random import randint


user = eval(input("0 is scissor, 1 is rock, 2 is paper"))
computer = randint(0,2)

if user == 0 and computer == 0:
    print("Draw, both scissor")
elif user == 0 and computer == 1:
    print("You win, with a scissor")
elif user == 0 and computer == 2:
    print("You lose, with a scissor")
elif user == 1 and computer == 0:
    print("You lose, with a rock")
elif user == 1 and computer == 1:
    print("Draw, both rock")
elif user == 1 and computer == 2:
    print("You win, with a rock")
elif user == 2 and computer == 0:
    print("You win, with a paper")
elif user == 2 and computer == 1:
    print("You lose, with a paper")
elif user == 2 and computer == 2:
    print("Draw, both paper")