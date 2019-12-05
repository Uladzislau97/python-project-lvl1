from brain_games.game_engine import run_game
from brain_games.utils import generate_random_number
from math import gcd

game_description = "Find the greatest common divisor of given numbers."


def generate_task():
    first_num = generate_random_number()
    second_num = generate_random_number()
    question = "{} {}".format(first_num, second_num)
    correct_answer = str(gcd(first_num, second_num))
    return {
        "question": question,
        "correct_answer": correct_answer
    }


def run_brain_gcd_game():
    run_game(game_description, generate_task)
