# Checking a number for parity.

from random import randint


RULE = "Answer 'yes' if the number is even, otherwise answer 'no'"


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def game_func():
    min_number = 2
    max_number = 100
    question = randint(min_number, max_number)
    correct_answer = is_even(question)
    return question, correct_answer
