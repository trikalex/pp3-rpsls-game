import random
import os
import sys


# Defining game variables
class Variables:
    """
    Game variables, winning combinatiions, graphics and scoreboard
    """
    # Game options list
    options = ["rock", "paper", "scissors", "lizard", "spock"]

    # Options dictionary
    options_dict = {
        1: "rock",
        2: "paper",
        3: "scissors",
        4: "lizard",
        5: "spock"
    }

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
        "scissors": "✂️ ",
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
        player_num = input(
            "Choose an option by number or by name: \n"
            "[1] for Rock, [2] for Paper,"
            "[3] for Scissors, [4] for Lizard, or [5] for Spock: "
        )
        comp = random.choice(Variables.options)

        # Check if the player's choice is valid
        if player_num.isdigit() and int(player_num) in Variables.options_dict:
            player = Variables.options_dict[int(player_num)].lower()
            break
        elif player_num.lower() in [value.lower() for value in Variables.options_dict.values()]:  # noqa
            player = player_num.lower()
            break
        else:
            print("Invalid choice! Please try again.")
            print('=====================================')
    reset_terminal()

    # Compare player's choice with comp's choice
    if comp in Variables.win_combis[player]:
        print(
            "You won! "
            f"{Variables.graphics[player]} beats {Variables.graphics[comp]}."
        )
        Variables.scoreboard["player"] += 1
    elif player == comp:
        print(
            "That's a draw! "
            f"Both players chose {Variables.graphics[player]}."
        )
    else:
        print(
            "You lost! "
            f"{Variables.graphics[comp]} beats {Variables.graphics[player]}."
        )
        Variables.scoreboard["computer"] += 1


def display_scoreboard():
    """
    Scoreboard function
    """
    print('Scoreboard:')
    print('=====================================')
    print(f"Player: {Variables.scoreboard['player']}")
    print('=====================================')
    print(f"Computer: {Variables.scoreboard['computer']}")
    print('=====================================')
    if Variables.scoreboard["computer"] < 5 and Variables.scoreboard["player"] < 5:  # noqa
        input('Please press enter to continue!')


# Keeping the score, prompting the player to play again 'y/n'
# Calling the end_game() function for the winner
def play_again():
    while True:
        again = input(
            "Do you want to play again? (yes/no)\n"
        ).lower()
        if len(again) == 0:
            reset_terminal()
            print("Invalid choice! Please try again.")
        elif again[0] == "y":
            for key in Variables.scoreboard:
                Variables.scoreboard[key] = 0
            return True
        elif again[0] == "n":
            reset_terminal()
            print('Thank you for playing!')
            sys.exit()
        else:
            reset_terminal()
            print("Invalid choice! Please try again.")


# Win or Loose situation function
def end_game():
    reset_terminal()
    if Variables.scoreboard["player"] == 5:
        print(
            "YOU WON!!!\n"
            "===========================================\n"
            "Congratiulations!\n"
            "==========================================="
        )
    else:
        print(
            "DEFEAT!\n"
            "===========================================\n"
            "Better luck next time!\n"
            "==========================================="
        )
    display_scoreboard()


def display_rules():
    """
    From the menu 1st option will display the game rules
    """
    print(
        "Rock Paper Scissor Lizard and Spock...\n"
        "===========================================\n"
    )
    print(
        "Rules are pretty simple:"
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


# Game load function
# Display menu options for user
def load_game():
    while True:
        reset_terminal()
        player = input(
            "Rock Paper Scissor Lizard and Spock...\n"
            "🧱  🧻  ✂️   🦎  🖖 \n"
            "===========================================\n"
            "Welcome to the game!\n"
            "===========================================\n"
            "Please choose an option:\n"
            "===========================================\n"
            "- Choose [1] for instructions!\n"
            "- Choose [2] for starting the game!\n"
            "- Choose [3] for quiting the game!\n"
        )
        options = ['1', '2', '3']
        if player in options:
            if player == '1':
                reset_terminal()
                display_rules()
                input("Please press enter to return back to the main menu!")
            elif player == '2':
                while True:
                    while Variables.scoreboard["computer"] < 5 and Variables.scoreboard["player"] < 5:  # noqa
                        play_game()
                        display_scoreboard()
                    end_game()
                    again = play_again()
                    if not again:
                        break
            elif player == '3':
                reset_terminal()
                print('Thank you for playing!')
                sys.exit()
        else:
            print("Invalid choice, please try again!")


load_game()
