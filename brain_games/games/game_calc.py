from brain_games.games import games_modul
from random import randint


RULE = "What is the result of the expression?"


def foo():
    rand_number_1 = randint(1, 10)
    rand_number_2 = randint(1, 10)
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

    print('Question: ', rand_quest)
    user_answer = int(input('Your answer: '))

    if games_modul.check_answer(user_answer, correct_answer):
        return True
    else:
        return False
