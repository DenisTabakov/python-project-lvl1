# Checking a number, prime or not.

from random import randint


# The rule of the game.
RULE = "Answer 'yes' if the number is primer, otherwise answer 'no'"

# Minimum number.
MIN_NUMBER = 2

# Maximum number.
MAX_NUMBER = 100


def is_prime(number):
    ''' Checks whether a number is prime. '''
    for k in range(2, number):
        if number % k == 0:
            return 'no'
    return 'yes'


def game_func():
    ''' Passes the question and the correct answer to the engine. '''
    question = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = is_prime(question)
    return question, correct_answer
