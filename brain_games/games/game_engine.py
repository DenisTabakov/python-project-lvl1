# Game scenario implementation.

from brain_games.games import games_modul


def engine_func(module_name):
    print(module_name.RULE)
    i = 1
    while i <= 3:
        if not module_name.foo():
            break
        if i == 3:
            print('{0}, {1}!'.format('Congratulations', games_modul.name))
        i += 1
