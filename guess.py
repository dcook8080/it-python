import random

print("=================")
print(" GUESS MY NUMBER ")
print(  "By Dylan Cook"  )
print("=================")
print("")

name = input("What is your name? ")
print(f"Hi, {name}")

print("")
the_number = random.randint(0, 100)

print("I'm thinking of an integer between 0 and 100. Can you guess it? ")

guess = -1

while guess != the_number:
    guess_text = input("What is your guess? ")
    guess = int(guess_text)

    if guess < the_number :
        print(f"Sorry {name}, your guess is too LOW, Try Again.")
    elif guess > the_number :
        print(f"Sorry {name}, your guess is too HIGH, Try Again.")
    else :
        print(f"You guessed it! Congratulations, {name}")
print("thanks for playing")