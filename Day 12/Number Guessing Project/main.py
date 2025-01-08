import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def number_guess_game(guessed_num, actual_num, turns):
    if guessed_num > actual_num:
         print('Too high.')
         return turns - 1
    elif guessed_num < actual_num:
        print('Too low.')
    else:
        print(f'You got it!. The answer was {actual_num}')


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print('I am thinking of numbers between 1 and 100.')
    answer = random.randint(1, 100)
    # print(f'Correct answer is {answer}')
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f'you have {turns} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))
        attempts = number_guess_game(guess, answer, turns)
        if attempts == 0:
            print(f'You have run out of guesses, you lose.')
            return
        elif guess != answer:
            print('Guess again.')


game()

