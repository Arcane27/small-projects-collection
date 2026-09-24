print("Welcome to Rock, Paper, Scissors!")
print("You can play against the computer or have the computer play against itself.")

def play_rps():
    user_input = input("Type 'p' to play against the computer, 'c' for the computer to play against itself, or 'n' to exit: ")
    if user_input.lower() == 'n':
        print("Thanks for playing!")
        return
    elif user_input.lower() == 'p':
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            return play_rps()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"The computer chose {computer_choice}.")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("You lose!")
    elif user_input.lower() == 'c':
        computer_choice1 = random.choice(['rock', 'paper', 'scissors'])
        computer_choice2 = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer 1 chose {computer_choice1}.")
        print(f"Computer 2 chose {computer_choice2}.")
        if computer_choice1 == computer_choice2:
            print("It's a tie!")
        elif (computer_choice1 == 'rock' and computer_choice2 == 'scissors') or \
             (computer_choice1 == 'paper' and computer_choice2 == 'rock') or \
             (computer_choice1 == 'scissors' and computer_choice2 == 'paper'):
            print("Computer 1 wins!")
        else:
            print("Computer 2 wins!")

play_rps()
