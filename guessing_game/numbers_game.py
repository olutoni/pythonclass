import random
print("Welcome to the number guessing game")
print("You only have four guesses")

# Initialize the number to be guessed
number_to_guess = random.randint(1, 10)

# Initialize the default number of tries the player has made
count_number_of_tries = 1

# Ask for the initial guess from the player
guess = int(input("Please guess a number between 1 and 10: "))

# If the guess is wrong, perform the following operations
while number_to_guess != guess:
    print("Sorry wrong number")

    # check if number of tries has exceeded and break out of the loop, otherwise provide feedback to the player
    if count_number_of_tries == 4:
        break
    elif guess < number_to_guess:
        print("Your guess was lower than the number")
    else:
        print("Your guess was higher than the number")

    # Ask player to try again and increment the number of attempts
    guess = int(input("Please try again: "))
    count_number_of_tries += 1

# Check if they guessed number is correct, tell the player they won if correct.
if number_to_guess == guess:
    print("Well done you won!")
    print(f"You took, {count_number_of_tries}, guess(es) to complete the game")
else:
    # if number of tries has been exceeded, then end the game and show the number to the player
    print("Sorry - you lose")
    print(f"The number you needed to guess was, {number_to_guess}")

print("Game Over!!!")
