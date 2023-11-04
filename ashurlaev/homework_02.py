def reverse(arg):
    otvet = []
    for peremenay1 in arg:
        otvet.insert(0, peremenay1)
    return otvet


def avglen(arg):
    peremenaya2 = 0
    for peremenay1 in arg:
        peremenaya2 += len(peremenay1)
    return peremenaya2 / len(arg)


def index(arg):
    otvet = {}
    for f, peremenay1 in enumerate(arg):
        if peremenay1 not in otvet.keys():
            otvet[peremenay1] = [f]
        else:
            otvet[peremenay1].append(f)
    for f in otvet.keys():
        if len(otvet[f]) == 1:
            copy = otvet[f][0]
            otvet[f] = copy
    return otvet


def coincidence(arg1, arg2):
    otvet = []
    for peremenay1 in arg1:
        if peremenay1 not in otvet:
            if peremenay1 in arg2:
                otvet.append(peremenay1)
    return otvet


def count(arg):
    otvet = {}
    for f in arg:
        if f not in otvet.keys():
            otvet[f] = 1
        else:
            otvet[f] += 1
    return otvet


def lensort(arg):
    otvet = arg
    length = len(otvet)
    for f in range(length - 1):
        for k in range(length - f - 1):
            if len(otvet[k]) > len(otvet[k + 1]):
                copy = otvet[k]
                otvet[k] = otvet[k + 1]
                otvet[k + 1] = copy
    return otvet