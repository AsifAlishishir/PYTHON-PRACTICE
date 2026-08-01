import random

print("🐍 SNAKE (S)   💧 WATER (W)   🔫 GUN (G) — Let the battle begin!\n")


# COMPUTER'S CHOICE
computer=random.choice([1,0,-1])

# TAKING INPUT FROM USER
yourChoiceInput=input("Enter your choice [S]nake / [W]ater / [G]un: ").strip().lower()


yourChoiceList={'s':1, 'w' :0, 'g': -1}

# CHECKING INVALID INPUT'S
while yourChoiceInput not in yourChoiceList:
    print("❌ Invalid choice! Please enter S, W, or G.")
    yourChoiceInput = input("Enter your choice [S]nake / [W]ater / [G]un: ").strip().lower()

# USER'S CHOICE
yourChoice=yourChoiceList[yourChoiceInput]
newDict={1:'Snake', 0:'Water', -1:'Gun'}
print(f"You Chose: {newDict[yourChoice]} \nComputer Chose: {newDict[computer]}")
# print(computer, yourChoice)


# now logic part
# Rules:
#   - Gun beats Snake   (বন্দুক সাপকে মারে)
#   - Snake beats Water (সাপ পানি খায়)
#   - Water beats Gun   (পানি বন্দুকে মরচে ধরায়)
# Same choice vs same choice = Draw.


if(computer == yourChoice):
    print("It's a Draw!")
else:
    if(computer == 1 and yourChoice == 0):
        print("Computer Won!")
    elif(computer == 1 and yourChoice == -1):
        print("You Won!")
    elif(computer == 0 and yourChoice == 1):
        print("You Won!")
    elif(computer == 0 and yourChoice == -1):
        print("Computer Won!")
    elif(computer == -1 and yourChoice == 0):
        print("You Won!")
    elif(computer == -1 and yourChoice == 1):
        print("Computer Won!")
    else:
        print("Something is Wrong!!!")
