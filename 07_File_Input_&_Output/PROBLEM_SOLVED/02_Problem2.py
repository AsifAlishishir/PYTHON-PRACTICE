import random

def game():
    print("You are playing the game...")
    score=random.randint(1, 100)
    print("Your Score is:", score)

    # FETCH THE HISCORE
    with open('hiScore.txt', 'r') as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0

    if(score>hiscore):
        # WRITE THE NEW HISCORE TO THE FILE
        with open('hiScore.txt', 'w') as f:
            f.write(str(score))

game()