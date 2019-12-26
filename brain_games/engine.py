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
        task_data = game.generate_task()
        question = task_data["question"]
        correct_answer = task_data["correct_answer"]

        print("Question: {}".format(question))
        given_answer = prompt.string("Your answer: ")

        if (given_answer != correct_answer):
            result = "'{}' is wrong answer ;(. Correct answer was '{}'."
            print(result.format(given_answer, correct_answer))
            return

        print("Correct!")
        question_number += 1

    print("Congratulations, {}!".format(name))
