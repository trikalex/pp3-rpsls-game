import random
import os

class Variables:
    """
    Game variables, winning combinatiions, graphics and scoreboard
    """
    # Game options list
    options = ["rock", "paper", "scissors", "lizard", "spock"]

    # Winning combinations dictionary
    win_combis = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["paper", "spock"],
        "spock": ["rock", "scissors"],
    }

    # ASCII graphics dictionary
    graphics = {
        "rock": "",
        "paper": "",
        "scissors": "",
        "lizard": "",
        "spock": "",
    }

    # Scoreboard
    scoreboard = {"player": 0, "computer": 0}

class Game:
    """ 
    Game Play elements and funcotions
    """
    # Gameplay function
    def play_game():
        player = input("Choose one: rock, paper, scissors, lizard, or spock: ").index(1)
        comp = random.choice(options)
        
        # Check if the player's choice is valid
        if player not in options:
            print("Invalid choice! Please try again.")
            print('=====================================')
            return play_game()
        
        # Compare player's choice with comp's choice
        if comp in win_combis[player]:
            print(f"You won! {graphics[player]} beats {graphics[comp]}.")
            scoreboard["player"] += 1
        elif player == comp:
            print(f"That's a draw! Both players chose {graphics[player]}.")
        else:
            print(f"You lost! {graphics[comp]} beats {graphics[player]}.")
            scoreboard["computer"] += 1

    # Scoreboard function
    def display_scoreboard():
        print('Scoreboard:')
        print('=====================================')
        print(f"Player: {scoreboard['player']}")
        print('=====================================')
        print(f"Computer: {scoreboard['computer']}")
        print('=====================================')

    # Terminal reset function
    def reset_terminal():
        os.system("cls" if os.name == "nt" else "clear")

    # Play the game
    while True:
        reset_terminal()
        play_game()
        display_scoreboard()
        
        # Ask player if they want to play again
        play_again = input("Do you want to play again? (yes/no) ").lower()
        if play_again != "yes":
            break
