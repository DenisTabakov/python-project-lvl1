from random import randint

RULE = "What number is missing in the progression?"

MIN_STEP = 1

MAX_STEP = 6

START_NUM = 1

LEN_PROG = 10


def get_progression():
    ''' generates an arithmetic progression '''

    step = randint(MIN_STEP, MAX_STEP)
    progression_list = []

    for value in range(START_NUM, LEN_PROG + 1):
        progression_list.append(str(value * step))

    return progression_list


def get_question_answer():
    ''' Passes the question and the correct answer to the engine. '''
    progression = get_progression()
    dot_position = randint(0, 9)
    correct_answer = progression[dot_position]
    progression[dot_position] = '..'
    question = ' '.join(progression)

    return question, correct_answer
