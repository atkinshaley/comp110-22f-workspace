""""An example of conditional (if-else) statemnts."""

SECRET: int = 3

print("I'm thinking of a value between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET: 
    print("You guessed correctly!!!")
    print("Have a wonderful day!!!")

else:
    if guess > 5:
        print("That's not even a choice dummy!")
        print("Try running the program again.")
    else:
        print("Sorry you guessed incorrectly. :(")
        print("Try running the program again.")

print("Game over.")