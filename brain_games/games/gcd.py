from brain_games.utils import generate_random_number

GAME_DESCRIPTION = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(a % b, b) if a >= b else gcd(a, b % a)


def generate_task():
    first_num = generate_random_number()
    second_num = generate_random_number()
    question = "{} {}".format(first_num, second_num)
    correct_answer = str(gcd(first_num, second_num))
    return {
        "question": question,
        "correct_answer": correct_answer
    }
