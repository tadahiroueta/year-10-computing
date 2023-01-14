def read(s):
    if 48 <= ord(s) < 58:
        return int(s)

    if 97 <= ord(s) < 103:
        return ord(s) - 87

    return ord(s) - 55


def write(n):
    if n < 10:
        return str(n)

    return chr(n + 55)


while True:
    print('[H]exa or [D]eca?')
    sys = input('>>>>    ')
    if sys == 'H' or sys == 'h':
        print('\nGo for it:')
        n = input('>>>>    ')
        print(16 * read(n[0]) + read(n[1]))

    elif sys == 'D' or sys == 'd':
        print('\nGo for it:')
        n = int(input('>>>>    '))
        print(write(n // 16) + write(n % 16))

    print()
