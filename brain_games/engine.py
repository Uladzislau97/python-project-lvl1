import prompt

MAX_NUMBER_OF_QUESTIONS = 3


def run(game):
    print("Welcome to the Brain Games!")
    print(game.GAME_DESCRIPTION)
    print()

    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    print()

    question_number = 1
    while question_number <= MAX_NUMBER_OF_QUESTIONS:
        question, correct_answer = game.generate_task()

        print("Question: {}".format(question))
        given_answer = prompt.string("Your answer: ")

        if given_answer != correct_answer:
            result = "'{}' is wrong answer ;(. Correct answer was '{}'."
            print(result.format(given_answer, correct_answer))
            return

        print("Correct!")
        question_number += 1

    print("Congratulations, {}!".format(name))
