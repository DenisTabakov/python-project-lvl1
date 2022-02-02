# Checking a number for parity.

from brain_games.games import games_modul


RULE = "Answer 'yes' if the number is even, otherwise answer 'no'"


def game_func():
    return games_modul.check_answer_long(games_modul.is_even)
