# Exercise 8

# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

pick1 = input("Player 1 - Rock, Paper, Scissors? ")
pick2 = input("Player 2 - Rock, Paper, Scissors? ")
if pick1 == pick2:
    print("It's a tie!")
elif pick1 == "Rock":
    if pick2 == "Paper":
        print("Paper beats Rock - Player 2 wins!")
    else:
        print("Rock beats Scissors - Player 1 wins!")
elif pick1 == "Paper":
    if pick2 == "Rock":
        print("Paper beats Rock - Player 1 wins!")
    else:
        print("Scissors beat Paper - Player 2 wins!")
elif pick1 == "Scissors":
    if pick2 == "Rock":
        print("Rock beats Scissors - Player 2 wins!")
    else:
        print("Scissors beat Paper - Player 1 wins!")
else:
    print("You have entered an invalid input!")