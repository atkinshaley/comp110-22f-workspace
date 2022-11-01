"""This exercise is a custom Wordle!"""


__author__ = "730480669"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, char: str) -> bool:
    """Determines if we have a string and a single character."""
    assert len(char) == 1
    i: int = 0
    while i < len(word):
        if word[i] == char:
            return True
        i = i + 1
    return False
    

def emojified(guess: str, secret_word: str) -> str:
    """Returns a codefied emoji string."""
    assert len(guess) == len(secret_word)
    j: int = 0
    emoji: str = ""
    while j < len(guess):
        if guess[j] == secret_word[j]:
            emoji = emoji + GREEN_BOX
            j = j + 1
        elif contains_char(secret_word, guess[j]):
            emoji = emoji + YELLOW_BOX
            j = j + 1
        else:
            emoji = emoji + WHITE_BOX
            j = j + 1
    return emoji


def input_guess(length: int) -> str:
    """This function determines if the guess is the correct amount of characters."""
    guess: str = input(f"Enter a {length} character word: ")
    valid: bool = False
    while not valid:
        if len(guess) == length:
            valid = True
        else:
            guess = input(f"That wasnt {length} chars! Try again: ")
    if valid:
        return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "haley"
    h: int = 1
    correct: str = "\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9"
    while h < 7:
        print(f"=== Turn {h}/6 ===")
        guess: str = input_guess(len(secret_word))
        if emojified(guess, secret_word) == correct:
            print(emojified(guess, secret_word))
            return print(f"You won in {h}/6 turns!")
        else:
            print(emojified(guess, secret_word))
            h = h + 1
    if h > 6:
        return print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()