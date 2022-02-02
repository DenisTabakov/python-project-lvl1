# Generating a pair of random numbers and three types of arithmetic operations.

from random import randint

from brain_games.games import games_modul


RULE = "What is the result of the expression?"


def game_func():
    min_number = 1
    max_number = 10
    rand_number_1 = randint(min_number, max_number)
    rand_number_2 = randint(min_number, max_number)
    k = randint(0, 2)
    list_st = [
        '{0} + {1}'.format(str(rand_number_1), str(rand_number_2)),
        '{0} - {1}'.format(str(rand_number_1), str(rand_number_2)),
        '{0} * {1}'.format(str(rand_number_1), str(rand_number_2)),
    ]
    list_i = [
        rand_number_1 + rand_number_2,
        rand_number_1 - rand_number_2,
        rand_number_1 * rand_number_2,
    ]
    rand_quest = list_st[k]
    correct_answer = list_i[k]

    print('Question: {}'.format(rand_quest))
    user_answer = int(input('Your answer: '))

    if games_modul.check_answer(user_answer, correct_answer):
        return True
    else:
        return False
