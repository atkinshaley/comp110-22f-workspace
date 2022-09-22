"""This exercise is like a wordle but with just one try."""
__author__ = "730480669"

secret_word: str = "python"
wrong: str = "Not quite. Play again soon!"
correct: str = "Woo! You got it!"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")

i: int = 0
emoji: str = ""
while i < len(secret_word):
    valid_2: bool = False
    if secret_word[i] == guess[i]:
        valid_2 = True
        emoji = emoji + GREEN_BOX  
    j: int = 0
    valid: bool = False
    while not valid and j < len(secret_word):
        if secret_word[j] == guess[i] and secret_word[i] != guess[i]:
            valid = True
        else:
            j = j + 1
    if valid:
        emoji = emoji + YELLOW_BOX
    if not valid_2 and not valid: 
        emoji = emoji + WHITE_BOX
    i = i + 1
print(emoji)

if (guess) == (secret_word):
    print(correct)
else:
    print(wrong)
