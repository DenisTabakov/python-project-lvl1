from random import randint


RULE = "Answer 'yes' if the number is even, otherwise answer 'no'"

MIN_NUMBER = 2

MAX_NUMBER = 100


def is_even(number):
    ''' parity check '''
    return number % 2 == 0


def get_question_answer():
    ''' Passes the question and the correct answer to the engine. '''

    question = randint(MIN_NUMBER, MAX_NUMBER)

    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
