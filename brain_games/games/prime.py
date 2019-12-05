from brain_games.game_engine import run_game
from brain_games.utils import generate_random_number
from math import floor, sqrt

game_description = \
    'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    min_prime_number = 2

    if (number < min_prime_number):
        return False

    max_possible_divider = floor(sqrt(number))

    for i in range(min_prime_number, max_possible_divider + 1):
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
    run_game(game_description, generate_task)
