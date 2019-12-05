from brain_games.game_engine import run_game
from brain_games.utils import generate_random_number

game_description = "What number is missing in the progression?"

progression_length = 10
min_progression_index = 0
max_progression_index = 9
min_common_difference = 1


def generate_sequence(first_element, common_difference):
    progression = []
    for i in range(progression_length):
        progression.append(first_element + common_difference * i)
    return progression


def generate_sequence_with_hidden_element(sequence, hidden_element_index):
    result = sequence[:]
    result[hidden_element_index] = ".."
    return result


def generate_task():
    first_element = generate_random_number()
    common_difference = generate_random_number(min_common_difference)
    sequence = generate_sequence(first_element, common_difference)
    hidden_element_index = generate_random_number(
        min_progression_index,
        max_progression_index
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
    run_game(game_description, generate_task)
