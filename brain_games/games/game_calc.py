from random import randint, choice
from operator import add, sub, mul


RULE = "What is the result of the expression?"

MIN_NUMBER = 1

MAX_NUMBER = 10


def calc(num_1, num_2, sign):
    ''' performs a mathematical operation on numbers '''
    operations = {'+': add, '-': sub, '*': mul}
    return operations[sign](num_1, num_2)


def get_question_answer():
    ''' Passes the question and the correct answer to the engine. '''

    rand_number_1 = randint(MIN_NUMBER, MAX_NUMBER)
    rand_number_2 = randint(MIN_NUMBER, MAX_NUMBER)

    sign = choice('+-*')

    question = '{0} {1} {2}'.format(str(rand_number_1), sign, str(rand_number_2))
    correct_answer = str(calc(rand_number_1, rand_number_2, sign))

    return question, correct_answer
