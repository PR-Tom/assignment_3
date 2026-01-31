import random


secret_number = random.randint(1, 10)

print("I'm thinking of a number between 1 and 10.")

while True:
    try:
        guess = int(input("What's your guess? "))

        if guess > secret_number:
            print("Too high!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Correct! You got it.")
            break
    except ValueError:
        print("Please enter an actual number.")
