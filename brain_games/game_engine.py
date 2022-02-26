import prompt

REPLAYS_NUM = 3


def engine(module_name):
    ''' game engine '''

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(module_name.RULE)

    for _ in range(REPLAYS_NUM):
        question, correct_answer = module_name.get_question_answer()
        print('Question: {}'.format(question))
        user_answer = str(input('Your answer: '))
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print("is wrong answer ;(. Correct answer was: ", correct_answer)
            print("Let's try again, {}!".format(name))
            return

    print('{0}, {1}!'.format('Congratulations', name))
