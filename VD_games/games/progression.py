import random

RULES = "What number is missing in the progression?"
PROGRESSION_LENGTH = 10
MIN_START = 1
MAX_START = 20
MIN_STEP = 1
MAX_STEP = 10


def generate_progression(start, step, length):
    progression = []

    for index in range(length):
        current_element = start + index * step
        progression.append(current_element)

    return progression


def get_question_and_answer():
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    progression = generate_progression(start, step, PROGRESSION_LENGTH)

    hidden_index = random.randint(0, PROGRESSION_LENGTH - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))

    return question, correct_answer
