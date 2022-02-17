# Generating a pair of random numbers and three types of arithmetic operations.

from random import randint


# The rule of the game.
RULE = "What is the result of the expression?"

# Minimum number of the range specified numbers.
MIN_NUMBER = 1

# Maximum number of the range specified numbers.
MAX_NUMBER = 10


def game_func():
    ''' Passes the question and the correct answer to the engine. '''
    rand_number_1 = randint(MIN_NUMBER, MAX_NUMBER)
    rand_number_2 = randint(MIN_NUMBER, MAX_NUMBER)

    k = randint(0, 2)
    # Random selection of a mathematical operation.

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
