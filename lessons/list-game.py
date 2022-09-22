"""Examples of using lists in a simple 'game'."""

from random import randint

rolls: list[int] = list() 
rolls.append(randint(1, 6))
rolls.append(randint(1, 6))
print(rolls)

# Access an individual item
print(rolls[0])
print(rolls[1])
print(len(rolls))
print(rolls[4])