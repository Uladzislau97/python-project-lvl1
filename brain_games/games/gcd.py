from brain_games.utils import generate_random_number
from math import gcd

GAME_DESCRIPTION = "Find the greatest common divisor of given numbers."


def generate_task():
    first_num = generate_random_number()
    second_num = generate_random_number()
    question = "{} {}".format(first_num, second_num)
    correct_answer = str(gcd(first_num, second_num))
    return {
        "question": question,
        "correct_answer": correct_answer
    }
