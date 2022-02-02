# Functions for implementing games.

import prompt
from random import randint


WELCOME = "Welcome to the Brain Games!"


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def is_even(number):
    return number % 2 == 0


def is_prime(number):
    for k in range(2, number):
        if number % k == 0:
            return False
    return True


def check_answer(user_answer, correct_answer):
    global name
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print("is wrong answer ;(. Correct answer was:", correct_answer)
        print("Let's try again,", name)
        return False


def check_answer_long(check_func):
    min_number = 2
    max_number = 100
    rand_number = randint(min_number, max_number)
    print('Question: {}'.format(str(rand_number)))
    user_answer = str(input('Your answer: '))
    if (check_func(rand_number) and user_answer == 'yes') or \
            (not check_func(rand_number) and user_answer == 'no'):
        print('Correct!')
        return True
    elif check_func(rand_number) and user_answer == 'no':
        print("Correct answer was 'yes'\nLet's try again, {}!".format(name))
        return False
    else:
        print("Correct answer was 'no'\nLet's try again, {}!".format(name))
        return False
