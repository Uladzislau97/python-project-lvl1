from brain_games.game_engine import run_game
from brain_games.utils import generate_random_number

GAME_DESCRIPTION = "What number is missing in the progression?"

PROGRESSION_LENGTH = 10
MIN_PROGRESSION_INDEX = 0
MAX_PROGRESSION_INDEX = 9
MIN_COMMON_DIFFERENCE = 1


def generate_sequence(first_element, common_difference):
    progression = []
    for i in range(PROGRESSION_LENGTH):
        progression.append(first_element + common_difference * i)
    return progression


def generate_sequence_with_hidden_element(sequence, hidden_element_index):
    result = sequence[:]
    result[hidden_element_index] = ".."
    return result


def generate_task():
    first_element = generate_random_number()
    common_difference = generate_random_number(MIN_COMMON_DIFFERENCE)
    sequence = generate_sequence(first_element, common_difference)
    hidden_element_index = generate_random_number(
        MIN_PROGRESSION_INDEX,
        MAX_PROGRESSION_INDEX
    )
    correct_answer = str(sequence[hidden_element_index])
    sequence_with_hidden_element = generate_sequence_with_hidden_element(
        sequence,
        hidden_element_index
    )
    question = " ".join(list(map(str, sequence_with_hidden_element)))
    return {
        "question": question,
        "correct_answer": correct_answer
    }


def run_brain_progression_game():
    run_game(GAME_DESCRIPTION, generate_task)
