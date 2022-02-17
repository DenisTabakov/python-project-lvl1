# Generating a pair of random numbers and the greatest common divisor.
# Generating a question, requesting an answer,
# verifying the correctness of the answer.

from random import randint

# The rule of the game.
RULE = "Find the greatest common divisor of given numbers"

# Minimum number of the range specified numbers.
MIN_NUMBER = 1

# Maximum number of the range specified numbers.
MAX_NUMBER = 10


def gr_common_divisor(number_1, number_2):
    ''' greatest common divisor '''
    def divisor_list_create(max_number):
        divisors = []
        for i in range(1, max_number + 1):
            if max_number % i == 0:
                divisors.append(i)
        return divisors
    list_1 = divisor_list_create(number_1)
    list_2 = divisor_list_create(number_2)
    return max(set(list_1) & set(list_2))


def game_func():
    ''' Passes the question and the correct answer to the engine. '''
    rand_number_1 = randint(MIN_NUMBER, MAX_NUMBER)
    rand_number_2 = randint(MIN_NUMBER, MAX_NUMBER)
    question = '{0} {1}'.format(str(rand_number_1), str(rand_number_2))
    correct_answer = str(gr_common_divisor(rand_number_1, rand_number_2))
    return question, correct_answer
