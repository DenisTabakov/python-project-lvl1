# Checking a number for parity.

from random import randint


# The rule of the game.
RULE = "Answer 'yes' if the number is even, otherwise answer 'no'"

# Minimum number.
MIN_NUMBER = 2

# Maximum number.
MAX_NUMBER = 100


def is_even(number):
    ''' parity check '''
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def game_func():
    ''' Passes the question and the correct answer to the engine. '''
    question = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = is_even(question)
    return question, correct_answer
