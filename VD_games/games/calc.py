import random

RULES = "What is the result of the expression?"
OPERATIONS = ("+", "-", "*")
MIN_NUMBER = 1
MAX_NUMBER = 100


def calculate(number_1, number_2, operation):
    match operation:
        case "+":
            return number_1 + number_2
        case "-":
            return number_1 - number_2
        case "*":
            return number_1 * number_2
        case _:
            raise ValueError("Unknown operation")


def get_question_and_answer():
    number_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(OPERATIONS)

    question = f"{number_1} {operation} {number_2}"
    correct_answer = str(calculate(number_1, number_2, operation))

    return question, correct_answer
