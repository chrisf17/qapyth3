import json


def get_questions():
    questions = None

    with open("questions.json") as fd:
        questions = json.load(fd)

    return questions


if __name__ == "__main__":

    my_questions = get_questions()
    total = 0
    correct = 0

    for question in my_questions["sport"]:
        print(question["question"])
        for option in question["options"]:
            print(f'\t{option}')
        answer = int(input("Enter your answer:"))
        if answer == question["answer"]:
            print("***Correct***")
            correct += 1
        else:
            print("---Not Correct---")
        total += 1

    print(f"{correct} out of a total of {total} correct answers")
