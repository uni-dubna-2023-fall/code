def reverse (arg):
    s = []
    i = len(arg)
    while i > 0:
        time = arg[i - 1]
        s.append(time)
        i -= 1
    return(s)


def avglen (arg):
    llist = len(arg)
    i = llist
    lword = 0
    while i > 0:
        p = len(arg[i - 1])
        lword += p
        i -= 1
    return(lword / llist)


def chekdict (dict, word):
    flag = 0
    for k in dict:
        if k == word:
            flag = 1
    return(flag)


def cheklist (liist, element):
    flag = 0
    for word in liist:
        if element == word:
            flag = 1
    return(flag)


def procheklist (liist, element):
    flag = 0
    for word in liist:
        if element == word:
            flag += 1
    return(flag)


def index (arg):
    dictionary = {}
    i = 0
    for word in arg:
        find = chekdict (dictionary, word)
        if find == 0:
            dictionary[word] = i
        else:
            chek = isinstance (dictionary[word], int)
            if chek == 0:
                dictionary[word].add (i)
            else:  
                k = set()
                k = {dictionary[word]}
                k.add(i)
                dictionary[word] = k
        i += 1
    return[dictionary]


def coincidence (arg1, arg2):
    sovpadenya = []
    for word in arg1:
        find1 = cheklist (arg2, word)
        find2 = cheklist (sovpadenya, word)
        if find1 == 1:
            if len(sovpadenya) != 0:
                if find2 == 0:
                    sovpadenya.append(word)
            else:
                sovpadenya.append(word)
    return(sovpadenya)


def count (arg):
    dictionary = {}
    for word in arg:
        f = procheklist (arg, word)
        z = chekdict (dictionary, word)
        if z == 0:
            dictionary[word] = f
    return dictionary


def lensort (arg):
    i = 1
    len = len(arg)
    result = []
    dictionary = {}
    for word in arg:
        dictionary[word] = len(word)
    while len(result) != len:
        for word in dictionary:
            if dictionary[word] == i:
                result.append(word)
        i += 1
    return(result)
