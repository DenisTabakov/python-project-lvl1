from brain_games.games import games_modul
from random import randint
from math import gcd


RULE = "Find the greatest common divisor of given numbers"


def foo():
    rand_number_1 = randint(1, 10)
    rand_number_2 = randint(1, 10)
    rand_quest = '{0} {1}'.format(str(rand_number_1), str(rand_number_2))
    correct_answer = gcd(rand_number_1, rand_number_2)
    print('Question: ', rand_quest)
    user_answer = int(input('Your answer: '))
    if games_modul.check_answer(user_answer, correct_answer):
        return True
    else:
        return False
