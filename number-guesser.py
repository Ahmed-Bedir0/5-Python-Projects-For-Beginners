import random

lowest_number = input("Type the lowest number: ")
highest_number = input("Type the highest number: ")

if lowest_number.lstrip("-").isdigit() and highest_number.lstrip("-").isdigit():
    lowest_number = int(lowest_number)
    highest_number = int(highest_number)

    if lowest_number >= highest_number:
        print("The lowest number must be smaller than the highest number.")
        quit()
else:
    print("Please type numbers next time.")
    quit()

random_number = random.randint(lowest_number, highest_number)
guesses = 0

while True:
    guesses += 1

    user_guess = input("Make a guess: ")

    if user_guess.lstrip("-").isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")
