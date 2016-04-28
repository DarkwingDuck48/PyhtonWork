import random


def game():
    card = [i for i in range(2,12)] * 4
    random.shuffle(card)
    count = 0
    countAI = 0
    while True:
        q = input("Take a card? Y or N\n")
        if q.lower() == "y":
            k = card.pop()
            print ("You take %s card" %k)
            count+=k
            if count > 21:
                print ("You lose. Result is %s" %count)
                break
            if count <21:
                print ("You result is %s" %count)
            if count == 21:
                print ("You win")
                break
        if q.lower() == 'n':
            print("You have %s points" %count)
            while countAI<=21:
                countres = countAI
                k=card.pop()
                countAI+=k
            if countres == 21:
                print ("AI have 21. You lose.")
            if count>countres:
                print ("You win. You result is",count, "AI result is",countres)
            if count < countres:
                print("You lose. You result is",count, "AI result is",countres)
            if count == countres:
                print('DRAW!!!')
            break
while True:
    q1 =input ("Do you want to test your luck? Y or N\n")
    if q1.lower() == 'y':
        game()
    if q1.lower() == 'n':
        print ("Good Bye")
        break