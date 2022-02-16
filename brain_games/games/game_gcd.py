# Generating a pair of random numbers and the greatest common divisor.
# Generating a question, requesting an answer,
# verifying the correctness of the answer.

from random import randint


RULE = "Find the greatest common divisor of given numbers"


def nod(number_1, number_2):
    ''' greatest common divisor '''
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


def game_func():
    min_number = 1
    max_number = 10
    rand_number_1 = randint(min_number, max_number)
    rand_number_2 = randint(min_number, max_number)
    question = '{0} {1}'.format(str(rand_number_1), str(rand_number_2))
    correct_answer = str(nod(rand_number_1, rand_number_2))
    return question, correct_answer
