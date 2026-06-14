import prompt

ROUNDS_COUNT = 3


def run_game(game):
    print("Welcome to the VD games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.RULES)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.get_question_and_answer()

        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
