import random

def roll_six_sided_die():
    print(f"You rolled a {random.randint(1,6)}")

def roll_custom_die(number_of_sides):
    print(f"You rolled a {random.randint(1, number_of_sides)}")

def roll_dice(sides, number_of_dice):
    rolls = [random.randint(1,sides) for _ in range(number_of_dice)]
    print(f"You rolled a {tuple(rolls)}")


print("Welcome to the dice rolling game!")
print("You can roll a six-sided die or a custom die with any number of sides.")
print("Type 'y' to roll a six-sided die, 'c' to roll a custom die, 'd' to roll multiple dice, or 'n' to exit the game.")
while True:
    user_input = input("Do you want to roll a six-sided die? (y/n/c/d): ")
    if user_input.lower() == 'n':
        print("Thanks for playing the game!")
        break
    elif user_input.lower() == 'y':
        roll_six_sided_die()
        continue
    elif user_input.lower() == 'c':
        while True:
            try:
                number_of_sides = int(input("Enter the number of sides for the custom die: "))
                if number_of_sides < 1:
                    print("Please input a positive integer greater than 0.")
                    continue
                roll_custom_die(number_of_sides)
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.")
    elif user_input.lower() == 'd':
        while True:
            try:
                sides = int(input("Enter the number of sides for the die: "))
                if sides < 1:
                    print("Please input a positive integer greater than 0.")
                    continue
                number_of_dice = int(input("Enter the number of dice to roll: "))
                if number_of_dice < 1:
                    print("Please input a positive integer greater than 0.")
                    continue
                roll_dice(sides, number_of_dice)
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.")
    else:
        print("Invalid input. Please enter 'y', 'n', 'c', or 'd'.")
