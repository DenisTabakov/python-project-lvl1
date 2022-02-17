# Generating an arithmetic progression in increments from 2 to 6
# and replacing a random term with dots.
# Generating a question, requesting an answer and verifying its
# correctness.

from random import randint


# The rule of the game.
RULE = "What number is missing in the progression?"

# Minimum progression step.
MIN_STEP = 1

# Maximum progression step.
MAX_STEP = 6

# The first member of the progression.
START = 1

# Progression length.
LEN_PROG = 10


def game_func():
    ''' Passes the question and the correct answer to the engine. '''

    # Random selection of the progression step.
    step = randint(MIN_STEP, MAX_STEP)

    # Random selection of the missing member of the progression.
    dot_position = randint(0, 9)

    g_list = []
    for value in range(START, LEN_PROG + 1):
        g_list.append(str(value * step))
    correct_answer = g_list[dot_position]
    g_list[dot_position] = '..'
    question = ' '.join(g_list)
    return question, correct_answer
