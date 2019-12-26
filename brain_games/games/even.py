from brain_games.utils import generate_random_number

GAME_DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_task():
    question = generate_random_number()
    correct_answer = "yes" if is_even(question) else "no"
    return {
        "question": question,
        "correct_answer": correct_answer
    }
