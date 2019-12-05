from brain_games.game_engine import run_game
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


def run_brain_even_game():
    run_game(GAME_DESCRIPTION, generate_task)
