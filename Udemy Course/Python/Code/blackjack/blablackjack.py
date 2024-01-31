import random 
import art 


def blackJack():

    print(art.logo)

    cards = {
        "hearts":{
            "nums":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],        
            "jack": 10,
            "queen": 10,
            "king": 10,
            "ace": 11
        },
        "spades":{
            "nums":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "jack": 10,
            "queen": 10,
            "king": 10,
            "ace": 11
        },
        "diamonds":{
            "nums":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "jack": 10,
            "queen": 10,
            "king": 10,
            "ace": 11
        },
        "clubs":{
            "nums":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "jack": 10,
            "queen": 10,
            "king": 10,
            "ace": 11
        }
    }

    scores = {
        "macine":0,
        "human":0
    }

    def goAgain():
        goAgain = input("Go again? (y/n)\n")

        if goAgain.lower() == "y":
            blackJack()
        else:
            quit()
            
    def cardPicking():
        family = random.choice(list(cards.keys()))
        types = random.choice(list(cards[family]))
        if types == "nums":
            pick = random.choice(list(cards[family][types]))
            cards[family][types].remove(pick)
        else:
            pick = cards[family][types]
            del cards[family][types]
        return pick

    def scoreCount(player):
        card = cardPicking()
        print(player,": ",card)
        if card == 11 and scores[player] + card >= 21:
            scores[player] += 1
        else:
            scores[player] += card
            if scores[player] == 21:
                print("You win")
                goAgain()

    ready = input("Are you ready to play? (y/n)")

    if ready != "n":
        scoreCount("macine")
        scoreCount("human")
        scoreCount("human")
        print(scores)
    else:
        quit()

    again = "y"

    while again != "n":
        again = input("Go again? (y/n)\n")
        if again.lower() == "n" or again.lower() != "y":
            break
        elif scores["human"] < 21:
            scoreCount("human")
            if scores["human"] == 21:
                print("Human wins")
                goAgain()
            elif scores["human"] > 21:
                print("Human loses")
                goAgain()
                
            else: 
                print(scores)
                
    while scores["macine"] < 17:
        scoreCount("macine")

    humanScore = 21 - scores["human"]
    macineScore = 21 - scores["macine"]

    if humanScore > macineScore and macineScore <=21:
        print("You lose")
        goAgain()
    elif humanScore == macineScore:
        print("Draw")
        goAgain()
    else:
        print("You win")
        goAgain()
    

blackJack()
