#!/usr/bin/env python

from brain_games.game_engine import engine
from brain_games.games import game_gcd


def main():
    engine(game_gcd)


if __name__ == '__main__':
    main()
