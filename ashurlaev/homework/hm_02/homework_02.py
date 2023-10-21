def reverse(arg):
    result = []
    for peremenay1 in arg:
        result.insert(0, peremenay1)
    return result


def avglen(arg):
    peremenaya2 = 0
    for peremenay1 in arg:
        peremenaya2 += len(peremenay1)
    return peremenaya2 / len(arg)


def index(arg):
    result = {}
    for f, peremenay1 in enumerate(arg):
        if peremenay1 not in result.keys():
            result[peremenay1] = [f]
        else:
            result[peremenay1].append(f)
    for f in result.keys():
        if len(result[f]) == 1:
            copy = result[f][0]
            result[f] = copy
    return result


def coincidence(arg1, arg2):
    result = []
    for peremenay1 in arg1:
        if peremenay1 not in result:
            if peremenay1 in arg2:
                result.append(peremenay1)
    return result


def count(arg):
    result = {}
    for f in arg:
        if f not in result.keys():
            result[f] = 1
        else:
            result[f] += 1
    return result


def lensort(arg):
    result = arg
    length = len(result)
    for f in range(length - 1):
        for k in range(length - f - 1):
            if len(result[k]) > len(result[k + 1]):
                copy = result[k]
                result[k] = result[k + 1]
                result[k + 1] = copy
    return result
