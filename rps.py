import random
from banner import banner

banner("Rock, Paper, Scissors" , "By Isiah and Dylan")
print("We are going to play Rock, Paper, Scissors. The first to win two out of three rounds is the winner")


def  prompt_player():
    print("")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    player_choice = int(input("What is your choice? "))
    return player_choice

def Results(player_choice, comp_choice):
    if player_choice == 1:
        if comp_choice ==1:
            print("It is a tie")

player_choice = prompt_player()
comp_choice = random.randint(1,3)
Results(player_choice, comp_choice)


