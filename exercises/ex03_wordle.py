"""This exercise is a custom Wordle!"""
__author__ = "730480669"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(guess: str, char: str) -> bool:
    """Determines if we have a string and a single character"""
    assert len(char) == 1
    i: int = 0
    while i < len(guess):
        if guess[i] == char:
            return True
        i = i + 1
    return False

def emojified(guess: str, secret_word: str) -> str:
    """Returns a codefied emoji string"""
    assert len(guess) == len(secret_word)
    j: int = 0
    emoji: str = ""
    while j < len(guess):
        if guess[j] == secret_word[j]:
            emoji = emoji + GREEN_BOX
            j = j + 1    
        while j < len(guess):
            if contains_char == True:            
                emoji = emoji + YELLOW_BOX
                j = j + 1
        if not contains_char:
            emoji = emoji + WHITE_BOX
            j = j + 1
    return emoji

