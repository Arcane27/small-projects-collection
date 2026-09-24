import random


def play_rps():
    options = ['r', 'p', 's']
    while True:
        computer_play = random.choice(options)
        user_input = input("\nChoose 'r' for rock, 'p' for paper, or 's' for scissors, 'q' to quite: ").lower(\
            )

        if user_input == 'q':
            print("\nThanks for playing!")
            break
        elif user_input == 'r':
            if computer_play == 'r':
                print("I played Rock, let's play again.")
                continue
            elif computer_play == 's':
                print("I played Scissors, you win. :(")
            elif computer_play == 'p':
                print("I played Paper, I win. :)")
        elif user_input == 'p':
            if computer_play == 'p':
                print("I played Paper, let's play again.")
                continue
            elif computer_play == 'r':
                print("I played Rock, you win. :(")
            elif computer_play == 's':
                print("I played Scissors, I win. :)")
        elif user_input == 's':
            if computer_play == 's':
                print("I played Scissors, let's play again.")
                continue
            elif computer_play == 'r':
                print("I played Rock, I win. :)")
            elif computer_play == 'p':
                print("I played Paper, you win. :(")
        else:
            print("Please give a valid INPUT!")

def playgame():
    print("Welcome to the ROCK, PAPER, SCISSORs - the game!")
    print("I don't think I need to explain the rules, so let's just start.")
    print("you choose 'r' for rock, 'p' for paper, or 's' for scissors (and 'q' if you want to quite)")
    print("I will also randomly choose one, I promise, I won't cheat... hahaha (evil smile)")

    play_rps()



playgame()

