__author__ = "730480669"

word: str = input("Enter a 5-character word:")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit() 
else:   
    letter: str = input("Enter a single character:")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:        
        print("Searching for " + letter + " in " + word)
        if letter == word[0]:
            print(letter + " found at index" + " 0")
        if letter == word[1]:
            print(letter + " found at index" + " 1")
        if letter == word[2]:
            print(letter + " found at index" + " 2")
        if letter == word[3]:
            print(letter + " found at index" + " 3")
        if letter == word[4]:
            print(letter + " found at index" + " 4")
        if letter not in word:
            print("No instances of " + letter + " found in "+ word)
    word_count = word.count(letter)
    if letter in word:
        if word_count == 1:
            print(str(word_count) + " instance of " + letter + " found in " + word)
        if word_count > 1:
            print(str(word_count) + " instances of " + letter + " found in " + word)
        
