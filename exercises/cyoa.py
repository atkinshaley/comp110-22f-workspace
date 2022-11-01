"""This is a create your own adventure program."""


__author__ = 730480669


from random import randint


GRIFF_EMOJI: str = "\U00002764 \U0001F981"
SLY_EMOJI: str = "\U0001F49A \U0001F40D"
RAVEN_EMOJI: str = "\U0001F499 \U0001F985"
HUFF_EMOJI: str = "\U0001F49B \U0001F99D"


points: int = 0
player: str = input("Hello! What is your name? ")
choice_a: str = "A"
choice_b: str = "B"
choice_c: str = "C"
choice_d: str = "D"
choice_e: str = "E"
quit_game: str = "X"


def greet() -> None:
    """This procedure greets the player."""
    global player
    print(player)
    greeting: str = input(f"Welcome {player}! Take this quiz to find out which Harry Potter House you will be sorted into in college. Reply C to Continue. Reply X at any time to quit. ")
    if greeting == "X":
        print(f"Sorry to see you go {player}! Play again soon.")
        exit()


def choice_one() -> None:
    """This procedure is the players first choice."""
    global points
    global choice_a
    global choice_b
    global choice_c
    global choice_d
    global choice_e
    global quit_game
    question_one: str = input(f"{player}, Which other college would you rather visit, {choice_a}. App State, {choice_b}. Wake Forest, {choice_c}. NC State, {choice_d}. Duke, or {choice_e}. IDK? Please respond with A, B, C, D, or E. ")
    if question_one == choice_a:
        points += 2
    if question_one == choice_b:
        points += 4
    if question_one == choice_c:
        points += 6
    if question_one == choice_d:
        points += 8
    if question_one == choice_e:
        points += 0
    if question_one == quit_game:
        print(f"Sorry to see you go {player}! Play again soon.")
        exit()
      

def choice_two() -> None:
    """This procedure is the players second choice."""
    global points
    global choice_a
    global choice_b
    global choice_c
    global choice_d
    global choice_e
    global quit_game
    question_two: str = input(f"{player}, Where would you visit going out on a Thursday night in Chapel Hill, {choice_a}. He's Not Here, {choice_b}. Tru, {choice_c}. MAW, {choice_d}. The Crunkleton, or {choice_e}. IDK? Please respond with A, B, C, D, or E. ")
    if question_two == choice_a:
        points += 2
    if question_two == choice_b:
        points += 4
    if question_two == choice_c:
        points += 6
    if question_two == choice_d:
        points += 8
    if question_two == choice_e:
        points += 0
    if question_two == quit_game:
        print(f"Sorry to see you go {player}! Play again soon.")
        exit()
    

def choice_three() -> None:
    """This procedure is the players third choice."""
    global points
    global choice_a
    global choice_b
    global choice_c
    global choice_d
    global choice_e
    global quit_game
    question_three: str = input(f"{player}, Which spell would you use to combat someone in a duel, {choice_a}. Crucio, {choice_b}. Expelliarmus, {choice_c}. Stupefy, {choice_d}. Protego, or {choice_e}. IDK?? Please respond with A, B, C, D, or E. ")
    if question_three == choice_a:
        points += 8
    if question_three == choice_b:
        points += 6
    if question_three == choice_c:
        points += 4
    if question_three == choice_d:
        points += 2
    if question_three == choice_e:
        points += 0
    if question_three == quit_game:
        print(f"Sorry to see you go {player}! Play again soon.")
        exit()
    

def choice_four() -> None:
    """This procedure is the players fourth choice."""
    global points
    global choice_a
    global choice_b
    global choice_c
    global choice_d
    global choice_e
    global quit_game
    question_four: str = input(f"{player}, What essential would you take with you on a backpacking trip, {choice_a}. First Aid Kit, {choice_b}. Bear Bag, {choice_c}. A Knife, {choice_d}. Water Filter, or {choice_e}. IDK? Please respond with A, B, C, D, or E. ")
    if question_four == choice_a:
        points += 2
    if question_four == choice_b:
        points += 6
    if question_four == choice_c:
        points += 8
    if question_four == choice_d:
        points += 4
    if question_four == choice_e:
        points += 0
    if question_four == quit_game:
        print(f"Sorry to see you go {player}! Play again soon.")
        exit()


def choice_five() -> None:
    """This procedure is the players fifth choice."""
    global points
    global choice_a
    global choice_b
    global choice_c
    global choice_d
    global choice_e
    global quit_game
    question_five: str = input(f"{player}, What is your drink of choice, {choice_a}. IPA, {choice_b}. Bourbon, {choice_c}. New Zealand Sav, {choice_d}. Butterbeer, or {choice_e}. IDK? Please respond with A, B, C, D, or E. ")
    if question_five == choice_a:
        points += 6
    if question_five == choice_b:
        points += 8
    if question_five == choice_c:
        points += 4
    if question_five == choice_d:
        points += 2
    if question_five == choice_e:
        points += 0
    if question_five == quit_game:
        print(f"Sorry to see you go {player}! Play again soon.")
        exit()


def points_total() -> None:
    """Adds up points and decides house."""
    global points
    if points == 0:
        points = randint(1, 40)
    if points > 0 and points < 14:
        print(f"Congratulations {player}, you are a Hufflepuff {HUFF_EMOJI}!")
    if points >= 14 and points < 22:
        print(f"Congratulations {player}, you are a Ravenclaw {RAVEN_EMOJI}!")
    if points >= 22 and points < 32:
        print(f"Congratulations {player}, you are a Griffindor {GRIFF_EMOJI}!")
    if points >= 32:
        print(f"Congratulations {player}, you are a Slytherin {SLY_EMOJI}!")


def main() -> None:
    """The entrypoint of the program and main game loop."""
    global points
    greet()
    choice_one()
    choice_two()
    choice_three()
    choice_four()
    choice_five()
    points_total()


if __name__ == "__main__":
    main()