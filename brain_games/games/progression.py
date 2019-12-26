from brain_games.utils import generate_random_number

GAME_DESCRIPTION = "What number is missing in the progression?"

PROGRESSION_LENGTH = 10
MIN_PROGRESSION_INDEX = 0
MAX_PROGRESSION_INDEX = 9
MIN_COMMON_DIFFERENCE = 1


def generate_task():
    first_element = generate_random_number()
    common_difference = generate_random_number(MIN_COMMON_DIFFERENCE)
    hidden_element_index = generate_random_number(
        MIN_PROGRESSION_INDEX,
        MAX_PROGRESSION_INDEX
    )

    sequence = []
    sequence_with_hidden_element = []
    for i in range(PROGRESSION_LENGTH):
        element = first_element + common_difference * i
        sequence.append(element)
        if i == hidden_element_index:
            sequence_with_hidden_element.append("..")
        else:
            sequence_with_hidden_element.append(element)

    correct_answer = str(sequence[hidden_element_index])
    question = " ".join(list(map(str, sequence_with_hidden_element)))
    return {
        "question": question,
        "correct_answer": correct_answer
    }
