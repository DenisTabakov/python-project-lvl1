#!/usr/bin/env python

from brain_games.game_engine import engine_func
from brain_games import games_modul
from brain_games import game_gcd


print(games_modul.WELCOME)
games_modul.welcome_user()


def main():
    engine_func(game_gcd)


if __name__ == '__main__':
    main()
