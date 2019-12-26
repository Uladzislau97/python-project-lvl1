from brain_games.utils import generate_random_number
import random
import operator

GAME_DESCRIPTION = "What is the result of the expression?"

arithmetic_operations = [
    ("+", operator.add),
    ("-", operator.sub),
    ("*", operator.mul)
]


def generate_task():
    first_num = generate_random_number()
    second_num = generate_random_number()
    sign, operation = random.choice(arithmetic_operations)
    question = "{} {} {}".format(first_num, sign, second_num)
    correct_answer = str(operation(first_num, second_num))
    return {
        "question": question,
        "correct_answer": correct_answer
    }
