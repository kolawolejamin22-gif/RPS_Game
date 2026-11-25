# This is a RPS game
import random
playerstate = 0
while playerstate < 1 | playerstate > 3:
    playerinput = input(
        "Enter option: \n"
        "1 for rock\n"
        "2 for paper\n"
        "3 for scissors\n"
        "4 for ..."
    )
    playerchoice = int(playerinput)

    if playerchoice < 1 | playerchoice > 3:
        print("invalid choice choose again")
    else:
        playerstate = playerchoice

options = [1,2,3]
# Your options
computerchoice = random.choice(options)
print(f"Computer choose: {computerchoice}")

if(playerchoice == 1 & computerchoice == 3):
    print(f"You win") 
elif(playerchoice == 1 & computerchoice == 3):
    print(f"You win") 
elif(playerchoice == 2 & computerchoice == 1):
    print("You win")
elif (playerchoice == 3 & computerchoice == 2):
    print("You win")
else:
    print("Computer Win")
