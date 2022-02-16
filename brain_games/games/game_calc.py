# Generating a pair of random numbers and three types of arithmetic operations.

from random import randint


RULE = "What is the result of the expression?"


def game_func():
    min_number = 1
    max_number = 10
    rand_number_1 = randint(min_number, max_number)
    rand_number_2 = randint(min_number, max_number)
    k = randint(0, 2)
    list_st = [
        '{0} + {1}'.format(str(rand_number_1), str(rand_number_2)),
        '{0} - {1}'.format(str(rand_number_1), str(rand_number_2)),
        '{0} * {1}'.format(str(rand_number_1), str(rand_number_2)),
    ]
    list_i = [
        rand_number_1 + rand_number_2,
        rand_number_1 - rand_number_2,
        rand_number_1 * rand_number_2,
    ]
    question = list_st[k]
    correct_answer = str(list_i[k])
    return question, correct_answer
