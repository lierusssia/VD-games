import math
import random

RULES = "Find the greatest common divisor of given numbers."
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_question_and_answer():
    number_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number_2 = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = f"{number_1} {number_2}"
    correct_answer = str(math.gcd(number_1, number_2))

    return question, correct_answer
