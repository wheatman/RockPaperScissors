import random

def play():
    play = True
    stats = {}
    stats["wins"] = 0
    stats["loses"] = 0
    stats["ties"] = 0
    stats["games"]=0
    names = {}
    names[1] = "Rock"
    names[2] = "Paper"
    names[3] = "Scissors"
    info = {}
    info["all"] = []
    while play:
        turn = "unknown"
        while type(turn)!= int:
            turn = raw_input('your move(Rock/Paper/Scissors) ')
            if turn == "Rock":
                turn = 1
            if turn == "Paper":
                turn = 2 
            if turn == "Scissors":
                turn = 3
            else:
                print "please eneter one of the provided choices"
        print "you threw ", names[turn]
        info["all"].append(turn)
        compTurn = computerTurn(info)
        print "the computer threw ", names[compTurn]
        result = win(turn, compTurn)
        stats = showStats(stats, result)
        play = raw_input("do you want to play again?(y/n)")=="y"

def showStats(stats, result):
    stats["games"]+=1
    if result == -1:
        stats["loses"]+=1
    if result == 0:
        stats["ties"]+=1
    if result == 1:
        stats["wins"]+=1
    print "you have won", 100*float(stats["wins"])/stats["games"],"% of the time"
    print "you have lost", 100*float(stats["loses"])/stats["games"],"% of the time"
    print "you have tied", 100*float(stats["ties"])/stats["games"],"%of the time"
    return stats


def computerTurn(info):
    numberRocks = len([item for item in info["all"] if item ==1])
    numberPapers = len([item for item in info["all"] if item ==2])
    numberScissors = len([item for item in info["all"] if item == 3])
    total = len(info["all"])
    return rand1_3(float(numberRocks)/total, float(numberPapers)/total, float(numberScissors)/total)

def toBeat(turn):
    if turn == 1:
        return 2
    if turn == 2:
        return 3
    if turn == 3:
        return 1

def rand1_3(prob1, prob2, prob3):
    lst = [0]*100
    for i in range(int(prob1*100)):
        lst[i] = 1
    for i in range(int(prob1*100), int(prob2*100)):
        lst[i] = 2
    for i in range(int(prob1*100), 100):
        lst[i] = 3
    rand = random.randint(0,99)
    return toBeat(lst[rand])
    

def win(player, comp):
    if player == 1:
        if comp == 1:
            print "its a tie"
            return 0
        if comp == 2:
            print "you lose"
            return -1
        if comp == 3:
            print "you win"
            return 1
    if player == 2:
        if comp == 2:
            print "its a tie"
            return 0
        if comp == 1:
            print "you win"
            return 1
        if comp == 3:
            print "you lose"
            return -1
    if player == 3:
        if comp == 3:
            print "its a tie"
            return 0
        if comp == 2:
            print "you win"
            return 1
        if comp == 1:
            print "you lose"
            return -1
    
    
    
