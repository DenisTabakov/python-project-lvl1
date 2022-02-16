# Checking a number, prime or not.

from random import randint


RULE = "Answer 'yes' if the number is primer, otherwise answer 'no'"


def is_prime(number):
    for k in range(2, number):
        if number % k == 0:
            return 'no'
    return 'yes'


def game_func():
    question = randint(2, 100)
    correct_answer = is_prime(question)
    return question, correct_answer
