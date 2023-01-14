bili = []
for i in range(8):
    bili.append(2 ** i)

bili.sort(reverse=True)


def hexato(s):
    if 48 <= ord(s) < 58:
        return int(s)

    if 97 <= ord(s) < 103:
        return ord(s) - 87

    return ord(s) - 55


def tohexa(n):
    if n < 10:
        return str(n)

    return chr(n + 55)


def bito(s):
    global bili
    stlf = 0
    for i in range(8):
        stlf += int\
                    (s[i]) * bili[i]

    return stlf

def tobi(n):
    global bili
    stlf = ''
    for i in bili:
        if n >= i:
            stlf += '1'
            n -= i

        else:
            stlf += '0'

    return stlf

print(bito('10011110'))

while True:
    print('[H]exa or [B]inary?')
    sys = input('>>>>    ')
    if sys == 'H' or sys == 'h':
        print('\nGo for it:')
        n = input('>>>>    ')
        print(tobi(16 * hexato(n[0]) + hexato(n[1])))

    elif sys == 'B' or sys == 'b':
        print('\nGo for it:')
        n = input('>>>>    ')
        n = bito(n)
        print(tohexa(n // 16) + tohexa(n % 16))

    print()
