import prompt

MAX_NUMBER_OF_QUESTIONS = 3


def ask_question(generate_task):
    question_number = 1
    while question_number <= MAX_NUMBER_OF_QUESTIONS:
        task_data = generate_task()
        question = task_data["question"]
        correct_answer = task_data["correct_answer"]

        print("Question: {}".format(question))
        given_answer = prompt.string("Your answer: ")

        if (given_answer != correct_answer):
            return {
                "is_victory": False,
                "given_answer": given_answer,
                "correct_answer": correct_answer
            }

        print("Correct!")
        question_number += 1

    return {"is_victory": True}


def run(game):
    print("Welcome to the Brain Games!")
    print(game.GAME_DESCRIPTION + "\n")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!\n".format(name))
    game_result = ask_question(game.generate_task)
    if game_result["is_victory"]:
        print("Congratulations, {}!".format(name))
    else:
        answer_template = "'{}' is wrong answer ;(. Correct answer was '{}'."
        given_answer = game_result["given_answer"]
        correct_answer = game_result["correct_answer"]
        print(answer_template.format(given_answer, correct_answer))
