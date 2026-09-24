import random


options_names = {'r':'Rock', 'p':'Paper','s':'Sciccors'}
emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}
choices = ['r', 'p', 's']
user_wins = 0
computer_wins = 0

def get_user_choice():
    while True:
        user_input = input("\nChoose 'r' for rock, 'p' for paper, or 's' for scissors, 'q' to quite: ").lower()
        if user_input in choices:
            return user_input
        elif user_input == 'q':
            print("Thanks for playing!")
            return None
        else:
            print("Please enter a valid input!")

def get_computer_choice():
    return random.choice(choices)


def display_choices(user_choice, computer_choice):
    print(f"You played {options_names[user_choice]} {emojis[user_choice]}")
    print(f"I played {options_names[computer_choice]} {emojis[computer_choice]}")
    print(f"{emojis[user_choice]}   X   {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    global user_wins, computer_wins

    if user_choice == computer_choice:
        print("Tie!")
    elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
        print("You win :_ ✅")
        user_wins += 1
    else:
        print ("You lose! hahaha... ❌")
        computer_wins += 1


def play_round():
    u = get_user_choice()
    if u is None:
        return False
    c = get_computer_choice()
    display_choices(u, c)
    determine_winner(u, c)
    return True

def play_game():
    print("Welcome to the ROCK, PAPER, SCISSORs - the game!")
    print("I don't think I need to explain the rules, so let's just start.")
    print("you choose 'r' for rock, 'p' for paper, or 's' for scissors (and 'q' if you want to quite)")
    print("I will also randomly choose one, I promise, I won't cheat... hahaha (evil smile)")

    while True:
        try:
            rounds = int(input("How many rounds do you want to play? "))
            if rounds > 0:
                break
            print("Please enter a positive number of rounds.")
        except ValueError:
            print("Please enter a valid number of rounds.")

    for _ in range(rounds):
        if not play_round():
            break
    print(f"You won {user_wins} rounds and lost {computer_wins} rounds. Thanks for playing!")



play_game()

