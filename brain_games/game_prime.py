from brain_games import games_modul


RULE = "Answer 'yes' if the number is primer, otherwise answer 'no'"


def foo():
    return games_modul.check_answer_long(games_modul.is_prime)
