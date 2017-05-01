def cows_and_bulls(a, b):
    a = [int(i) for i in str(a)]
    b = [int(i) for i in str(b)]

    cows = 0
    bulls = 0

    c = []
    d = []

    for i in range(0, len(a)):
        if a[i] == b[i]:
                cows += 1
        else:
            c.append(a[i])
            d.append(b[i])

    for i in range(0, len(c)):
        if c[i] in d:
            bulls += 1
            d.remove(c[i])


    return cows, bulls




print(cows_and_bulls(1523, 2531))