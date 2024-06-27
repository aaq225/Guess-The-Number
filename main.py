from art import logo
import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high...")
        return turns - 1
    if guess < answer:
        print("Too low...")
        return turns - 1
    else:
        print(f"Correct!!! Answer is {answer}")
        
def set_difficulty():
    level = input("Choose 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS
    
def game():
    print(logo)
    print("Welcome to Guess The Number!")
    print("I am thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    turns = set_difficulty()
    guess = 0
    while guess !=answer:
        print(f"You have {turns} attempts remaining.")
        
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("No more guesses. You lose....")
            return
        elif guess != answer:
            print("Guess again: ")

game()
    