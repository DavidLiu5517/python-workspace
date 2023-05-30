import random as r
def start():
    word = ["like", 'bet', 'eat', 'big']
    return word[r.randint(0,3)]

def guess(wo):
    dig = ''
    for i in range(len(wo)):
        dig +='*'
    count = 0
    while True:
        v = eval(input(f"(Guess) Entry a letter in word {dig}"))
        c = 0
        if v in wo:
            for i in range(len(wo)):
                if wo[i] == v & dig[i] != v:
                    dig[i] = v
                elif wo[i] == v & dig[i] == v & c == 0:
                    c += 1
                    print(f'{v} is in the word')
        else:
            count += 1
            print(f"{v} is not in the word")
        if dig == wo & count > 1:
            print(f"{wo} is the word. You missed {count} times")
            print('')
            return 'Do you want to guess another word? Entry y or n'
        elif dig == wo:
            print(f"{wo} is the word. You missed {count} time")
            print('')
            return 'Do you want to guess another word? Entry y or n'

def main():
    wo = start()
    a = input(guess(wo))
    if a == 'y':
        main()

main()