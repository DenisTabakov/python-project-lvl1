# Game scenario implementation.

import prompt


WELCOME = "Welcome to the Brain Games!"


def check_answer(user_answer, correct_answer, name):
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print("is wrong answer ;(. Correct answer was:", correct_answer)
        print("Let's try again, {}!".format(name))
        return False


def engine_func(module_name):
    print(WELCOME)
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(module_name.RULE)
    i = 1
    while i <= 3:
        question, correct_answer = module_name.game_func()
        print('Question: ', question)
        user_answer = str(input('Your answer: '))
        if not check_answer(user_answer, correct_answer, name):
            break
        if i == 3:
            print('{0}, {1}!'.format('Congratulations', name))
        i += 1
