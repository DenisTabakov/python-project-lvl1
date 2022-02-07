#!/usr/bin/env python

from brain_games.games.game_engine import engine_func
from brain_games.games import games_modul
from brain_games.games import game_progression


def main():
    engine_func(game_progression)


if __name__ == '__main__':
    main()
