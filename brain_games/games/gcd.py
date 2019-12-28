from brain_games.utils import generate_random_number

GAME_DESCRIPTION = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        return b
    if b == 0:
        return a


def generate_task():
    first_num = generate_random_number()
    second_num = generate_random_number()
    question = "{} {}".format(first_num, second_num)
    correct_answer = str(gcd(first_num, second_num))
    return (question, correct_answer)
