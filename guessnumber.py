# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check(turn, guess, answer):
    if guess > answer:
        print("You're too high")
        return turn -1
    elif guess < answer:
        print("You're too low")
        return turn -1
    else:
        print (f"You got it. The number is {answer}")


def set():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ") 
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100." )
    answer = randint(1, 100)
    print(f"The correct answer is {answer}")
    turn = set()
    guess = 0
    while guess != answer:
        print(f"You have {turn} left.")
        guess = int(input("Make a guess: "))
        turn = check(turn, guess, answer)
        if turn == 0:
            print ("You out of turn. You lose")
        elif guess != answer:
            print ("Make a guess")
game()