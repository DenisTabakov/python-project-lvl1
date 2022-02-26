from random import randint


RULE = "Answer 'yes' if the number is primer, otherwise answer 'no'"

MIN_NUMBER = 2

MAX_NUMBER = 100


def is_prime(number):
    ''' Checks whether a number is prime. '''
    for k in range(2, number):
        if number % k == 0:
            return False
    return True


def get_question_answer():
    ''' Passes the question and the correct answer to the engine. '''

    question = randint(MIN_NUMBER, MAX_NUMBER)

    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
