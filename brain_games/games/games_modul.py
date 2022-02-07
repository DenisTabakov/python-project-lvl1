# Functions for implementing games.

import prompt
from random import randint


WELCOME = "Welcome to the Brain Games!"


def welcome():
    global name
    print(WELCOME)
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def is_even(number):
    return number % 2 == 0


def nod(number_1, number_2):
    list_1 = []
    list_2 = []
    for i in range(1, number_1 + 1):
        if number_1 % i == 0:
            list_1.append(i)
    for k in range(1, number_2 + 1):
        if number_2 % k == 0:
            list_2.append(k)
    list_common = list(set(list_1) & set(list_2))
    return max(list_common)


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
        print("Let's try again, {}!".format(name))
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
