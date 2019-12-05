from brain_games.game_engine import run_game
from brain_games.utils import generate_random_number
from math import floor, sqrt

GAME_DESCRIPTION = \
    'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    MIN_PRIME_NUMBER = 2

    if (number < MIN_PRIME_NUMBER):
        return False

    max_possible_divider = floor(sqrt(number))

    for i in range(MIN_PRIME_NUMBER, max_possible_divider + 1):
        if (number % i == 0):
            return False
    return True


def generate_task():
    question = generate_random_number()
    correct_answer = "yes" if is_prime(question) else "no"
    return {
        "question": question,
        "correct_answer": correct_answer
    }


def run_brain_prime_game():
    run_game(GAME_DESCRIPTION, generate_task)
