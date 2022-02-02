# Generating a pair of random numbers and the greatest common divisor.
# Generating a question, requesting an answer,
# verifying the correctness of the answer.

from random import randint
from math import gcd

from brain_games.games import games_modul


RULE = "Find the greatest common divisor of given numbers"


def game_func():
    min_number = 1
    max_number = 10
    rand_number_1 = randint(min_number, max_number)
    rand_number_2 = randint(min_number, max_number)
    rand_quest = '{0} {1}'.format(str(rand_number_1), str(rand_number_2))
    correct_answer = gcd(rand_number_1, rand_number_2)

    print('Question: ', rand_quest)
    user_answer = int(input('Your answer: '))

    if games_modul.check_answer(user_answer, correct_answer):
        return True
    else:
        return False
