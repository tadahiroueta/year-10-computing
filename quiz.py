from random import randint


def pick_operator():
    operator_list = [
        "+", "-", "*"
    ]
    return operator_list[randint(0, 2)]


def calculate(n1, n2, operator):
    if operator == "+":
        return n1 + n2

    if operator == "-":
        return n1 - n2

    return n1 * n2


def respond(answer, result):
    if answer == result:
        print("Correct!")
        return True

    print("Incorrect! = {}".format(result))
    return False


def quiz():
    print()
    score = 0
    for question in range(10):
        n1, n2 = randint(1, 100), randint(1, 100)
        operator = pick_operator()

        print("{} {} {}".format(n1, operator, n2))
        answer = int(input("= "))
        print()
        result = calculate(n1, n2, operator)
        if respond(answer, result): score += 1

    return score


def main():
    name = input("What is your name? ")
    total = 0
    while True:
        temporary_points = quiz()
        print()
        print("You scored {} / 10".format(temporary_points))
        total += temporary_points
        print("You have a total of {} points".format(total))
        if input("Would you like to do another quiz? [y/n] ") == "n":
            break


if __name__ == "__main__":
    main()
