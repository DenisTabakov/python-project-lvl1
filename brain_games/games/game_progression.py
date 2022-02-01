# Generating an arithmetic progression in increments from 2 to 6
# and replacing a random term with dots.
# Generating a question, requesting an answer and verifying its
# correctness.

from random import randint

from brain_games.games import games_modul



RULE = "What number is missing in the progression?"


def foo():
    step_list = randint(2, 6)
    dot_position = randint(0, 9)
    g_list = []

    for value in range(1, 11):
        g_list.append(str(value * step_list))

    correct_answer = g_list[dot_position]
    g_list[dot_position] = '..'
    str_list = ' '.join(g_list)

    print(str_list)
    user_answer = str(input('Your answer: '))

    if games_modul.check_answer(user_answer, correct_answer):
        return True
    else:
        return False
