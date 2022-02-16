# Generating an arithmetic progression in increments from 2 to 6
# and replacing a random term with dots.
# Generating a question, requesting an answer and verifying its
# correctness.

from random import randint


RULE = "What number is missing in the progression?"


def game_func():
    step_list = randint(1, 6)
    dot_position = randint(0, 9)
    g_list = []
    for value in range(1, 11):
        g_list.append(str(value * step_list))
    correct_answer = g_list[dot_position]
    g_list[dot_position] = '..'
    question = ' '.join(g_list)
    return question, correct_answer
