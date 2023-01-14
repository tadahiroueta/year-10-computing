def bubble(array):
    for pas in range(len(array)):
        change = False
        print(pas, array)
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                change = True

        if not change:
            print(pas + 1, array)
            return array


def insert(array):
    for pas in range(len(array)):
        for i in range(pas - 1, -1, -1):
            if array[pas] > array[i]:
                array.insert(i + 1, array[pas])
                array.pop(pas + 1)
                break

        else:
            array.insert(0, array[pas])
            array.pop(pas + 1)

        print(pas, array)

    return array


def merge(array):
    array, turn = breakme(array)
    for pas in range(len(array)):
        print(pas + turn, array)
        new = []
        for i in range(len(array) // 2):
            new_value = []
            try:
                for j in range(len(array[i * 2]) * 2):
                    if array[i * 2][0] < array[i * 2 + 1][0]:
                        new_value.append(array[i * 2][0])
                        array[i * 2].pop(0)

                    else:
                        new_value.append(array[i * 2 + 1][0])
                        array[i * 2 + 1].pop(0)

            except IndexError:
                if len(array[i * 2]) > 0:
                    for j in array[i * 2]:
                        new_value.append(j)

                else:
                    for j in array[i * 2 + 1]:
                        new_value.append(j)

            new.append(new_value)

        if len(array) % 2 == 1:
            new.append(array[-1])

        array = new

        if len(array) == 1:
            array = array[0]
            print(pas, array)
            return array


# part of merge
def breakme(array):
    array = [array]
    turn = 0
    while len(array[0]) > 1:
        print(turn, array)
        for i in range(len(array)):
            array.append(array[0][: len(array[0]) // 2])
            array.append(array[0][len(array[0]) // 2:])
            array.pop(0)

        turn += 1

    return array, turn


array = [63,45,73,23,81,18]
insert(array)
