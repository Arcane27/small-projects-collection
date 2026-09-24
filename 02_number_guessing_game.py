import random



def guess_number():
    number = random.randint(1,100)
    while True:
        try:
            guess = int(input("Guess the number between 1 and 100: "))
            if guess < 1 or guess > 100:
                print("Please enter a whole number between 1 and 100")
                continue
        except ValueError:
            print("Please enter a whole number between 1 and 100")
            continue

        if guess == number:
            print("YES! You guessed right and WON!")
            break
        elif guess < number:
            print("Your guess is too low...")
        elif guess > number:
            print("Your guess is too high...")

def computer_guess_number():
    print("Alright! Please think of a number between 1 and 100 and I will try to guess it.")
    print("I bet I can guess it in at most 7 guesses! Hahaha... (evil laugh)")
    input("Press ENTER when you're ready...")
    low, high = 1, 100
    count = 1
    while True:
        guess = (low + high) // 2
        print(f"{count}. {guess}")
        count += 1
        u_i = input("choose (l/h/r):\n'l' for my guess is too low,\n'h' for my guess is too high,\n'r' if I got it right:\n")
        if u_i == 'l':
            low = guess + 1
        elif u_i == 'h':
            high = guess - 1
        elif u_i == 'r':
            print("Yes!!! I got it right.")
            break
        else:
            print("Please enter a valid Input (l/h/r).")


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Do you want to guess or have the computer guess your number?")
    while True:
        user_input = input("Type 'g' to guess or 'c' for the computer to guess:  and 'q' to quite the game: ")
        if user_input.lower() == 'g':
            guess_number()
        elif user_input.lower() == 'c':
            computer_guess_number()
        elif user_input == 'q':
            print("Thanks for playing the Number Guessing Game!")
            break
        else:
            print("Please enter a valid input (g/c/q)")

number_guessing_game()
