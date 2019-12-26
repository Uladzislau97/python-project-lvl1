from brain_games.utils import generate_random_number

MIN_SIGN_INDEX = 0
MAX_SIGN_INDEX = 2
GAME_DESCRIPTION = "What is the result of the expression?"

arithmetic_signs = ["+", "-", "*"]
arithmetic_operations_by_sign = {
    "+": lambda first_num, second_num: first_num + second_num,
    "-": lambda first_num, second_num: first_num - second_num,
    "*": lambda first_num, second_num: first_num * second_num
}


def generate_random_arithmetic_sign():
    random_index = generate_random_number(MIN_SIGN_INDEX, MAX_SIGN_INDEX)
    return arithmetic_signs[random_index]


def generate_task():
    first_num = generate_random_number()
    second_num = generate_random_number()
    sign = generate_random_arithmetic_sign()
    question = "{} {} {}".format(first_num, sign, second_num)
    operation = arithmetic_operations_by_sign[sign]
    correct_answer = str(operation(first_num, second_num))
    return {
        "question": question,
        "correct_answer": correct_answer
    }
