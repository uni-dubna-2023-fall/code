def reverse(arg):
    s = []
    i = len(arg)
    while i > 0:
        time = arg[i - 1]
        s.append(time)
        i -= 1
    return s


def avglen(arg):
    llist = len(arg)
    i = llist
    lword = 0
    while i > 0:
        p = len(arg[i - 1])
        lword += p
        i -= 1
    return lword / llist


def index(arg):
    dictionary = {}
    i = 0
    for word in arg:
        if word not in dictionary:
            dictionary[word] = i
        else:
            chek = isinstance(dictionary[word], int)
            if chek is False:
                dictionary[word].append(i)
            else:
                k = [dictionary[word]]
                k.append(i)
                dictionary[word] = k
        i += 1
    return dictionary


def coincidence(arg1, arg2):
    along = []
    for word in arg1:
        if word in arg2:
            if len(along) != 0:
                if word not in along:
                    along.append(word)
            else:
                along.append(word)
    return along


def count(arg):
    dictionary = {}
    for word in arg:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    return dictionary


def lensort(arg):
    diction = {}
    result = []
    max_len = 0
    for word in arg:
        keylen = len(word)
        if keylen in diction:
            diction[keylen].append(word)
        else:
            diction[keylen] = [word]
        max_len = max(max_len, keylen)
    for word in range(max_len + 1):
        if word in diction:
            result.extend(diction[word])
    return result
