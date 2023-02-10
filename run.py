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
        "rock": "🧱",
        "paper": "🧻",
        "scissors": "✂️",
        "lizard": "🦎",
        "spock": "🖖",
    }

    # Scoreboard
    scoreboard = {"player": 0, "computer": 0}


# Game
# Terminal reset function
def reset_terminal():
    os.system("cls" if os.name == "nt" else "clear")


# Gameplay function
def play_game():
    while True:
        reset_terminal()
        player = input("Choose one: Rock, Paper, Scissors, Lizard, or Spock: ").lower()
        comp = random.choice(Variables.options)

        # Check if the player's choice is valid
        if player in Variables.options:
            break
        else:
            print("Invalid choice! Please try again.")
            print('=====================================')

    # Compare player's choice with comp's choice
    if comp in Variables.win_combis[player]:
        print(f"You won! {Variables.graphics[player]} beats {Variables.graphics[comp]}.")
        Variables.scoreboard["player"] += 1
    elif player == comp:
        print(f"That's a draw! Both players chose {Variables.graphics[player]}.")
    else:
        print(f"You lost! {Variables.graphics[comp]} beats {Variables.graphics[player]}.")
        Variables.scoreboard["computer"] += 1
    display_scoreboard()


# Scoreboard function
def display_scoreboard():
    print('Scoreboard:')
    print('=====================================')
    print(f"Player: {Variables.scoreboard['player']}")
    print('=====================================')
    print(f"Computer: {Variables.scoreboard['computer']}")
    print('=====================================')


def play_again():
    if Variables.scoreboard["computer"] >= 10 or Variables.scoreboard["player"] >= 10:
        return False
    else:

        while True:
            again = input("Do you want to play again? (yes/no) ").lower()
            if again[0] == "y":
                return True
            elif again == "n":
                return False
            else:
                reset_terminal()
                print("Invalid choice! Please try again.")


def display_rules():
        print("Rock Paper Scissor Lizard and Spock...\n"
            "===========================================\n"
            "Welcome to the game!\n"
            "==========================================="
        )
        print(
            "Rules are pretty simple..."
        )
        print(
            "===========================================\n"
            "Rock crushes Scissors, Rock crushes Lizard, \n"
            "Paper covers Rock, Paper disproves Spock, \n"
            "Scissors decapitate Lizard, Scissors cuts Paper, \n"
            "Lizard poisons Spock, Lizard eats Paper,\n"
            "Spock smashes Scissors, Spock vaporizes Rock.\n"
            "==========================================="
        )

def load_game():
    while True:
        reset_terminal()
        player = input(
            "Please choose an option:\n"
            "- Choose 1 for instructions!\n"
            "- Choose 2 for starting the game!\n"
            "- Choose 3 for quiting the game!\n"
        )
        options = ['1', '2', '3']
        if player in options:
            if player == '1':
                reset_terminal()
                display_rules()
                input("Please press enter to return back to the main menu!")
            elif player == '2':
                while True:
                    play_game()
                    again = play_again()
                    if not again:
                        break
            elif player == '3':
                print('Thank you for playing')
                break
        else:
            print("Invalid choice! Please try again.")


load_game()
