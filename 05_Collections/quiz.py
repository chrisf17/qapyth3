import json


def get_questions():
    questions = None

    with open("questions.json") as fd:
        questions = json.load(fd)

    return questions


if __name__ == "__main__":

    my_questions = get_questions()
    # To Do
    # Using input and Dictionary navigation
    # Build an interactive quiz
    # Take a look at questions.json
