# Game scenario implementation.

import prompt

# User's greeting.
WELCOME = "Welcome to the Brain Games!"

# Number of replays of games.
REPLAYS_NUM = 3


def check_answer(user_answer, correct_answer, name):
    ''' Checks the correctness of the user's response. '''
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print("is wrong answer ;(. Correct answer was:", correct_answer)
        print("Let's try again, {}!".format(name))
        return False


def engine_func(module_name):
    ''' Game engine - game scenario implementation.'''
    print(WELCOME)
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(module_name.RULE)
    i = 1
    while i <= REPLAYS_NUM:
        question, correct_answer = module_name.game_func()
        print('Question: ', question)
        user_answer = str(input('Your answer: '))
        if not check_answer(user_answer, correct_answer, name):
            break
        if i == REPLAYS_NUM:
            print('{0}, {1}!'.format('Congratulations', name))
        i += 1
