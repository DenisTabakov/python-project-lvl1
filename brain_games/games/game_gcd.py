from random import randint


RULE = "Find the greatest common divisor of given numbers"

MIN_NUMBER = 1

MAX_NUMBER = 10


def gcd(num1, num2):
    ''' calculates the greatest common divisor '''
    if num1 == 0:
        return num2
    return gcd(num2 % num1, num1)


def get_question_answer():
    ''' Passes the question and the correct answer to the engine. '''

    rand_number_1 = randint(MIN_NUMBER, MAX_NUMBER)
    rand_number_2 = randint(MIN_NUMBER, MAX_NUMBER)

    question = '{0} {1}'.format(str(rand_number_1), str(rand_number_2))
    correct_answer = str(gcd(rand_number_1, rand_number_2))

    return question, correct_answer
