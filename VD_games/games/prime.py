import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def get_question_and_answer():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = "yes" if is_prime(number) else "no"

    return str(number), correct_answer
