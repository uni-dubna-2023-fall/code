def reverse(arg):
    s = []
    i = len(arg)
    while i > 0:
        time = arg[i - 1]
        s.append(time)
        i -= 1
    return(s)
def avglen(arg):
    llist = len(arg)
    i = llist
    lword = 0
    while i > 0:
        p = len(arg[i - 1])
        lword += p
        i -= 1
    return(lword / llist)

# dop function
def chekdict(dict, word):
    flag = 0
    for k in dict.keys():
        if k == word:
            flag = 1
    return(flag)
def cheklist(liist, element):
    flag = 0
    for word in liist:
        if element == word:
            flag = 1
    return(flag)
def procheklist(liist, element):
    flag = 0
    for word in liist:
        if element == word:
            flag += 1
    return(flag)

def smallest(llist, element):
    for word in llist:
        if len(element) > len(word):
            return(0)
    return(1)
def findsmallest(llist):
    i = 0
    for word in llist:
        k = smallest(llist, word)
        if k == 1:
            return(i)
        i += 1


def index(arg):
    dictionary = {}
    i = 0
    for word in arg:
        find = chekdict(dictionary, word)
        if find == 0:
            dictionary[word] = i
        else:
            l = isinstance(dictionary[word], int)
            if l == 0:
                dictionary[word].add(i)
            else:  
                k = set()
                k = {dictionary[word]}
                k.add(i)
                dictionary[word] = k
        i += 1
    return[dictionary]

def coincidence(arg1, arg2):
    sovpadenya = []
    for word in arg1:
        find1 = cheklist(arg2, word)
        find2 = cheklist(sovpadenya, word)
        if find1 == 1:
            if len(sovpadenya) != 0:
                if find2 == 0:
                  sovpadenya.append(word)
            else:
                sovpadenya.append(word)
    return(sovpadenya)

def count(arg):
    dictionary = {}
    for word in arg:
        f = procheklist(arg, word)
        z = chekdict(dictionary, word)
        if z == 0:
            dictionary[word] = f
    return dictionary

def lensort(arg):
    i = len(arg)
    result = []
    clone = arg
    while i > 0:
        num = findsmallest(clone)
        result.append(clone[num])
        clone.pop(num)
        i -= 1
    return(result)
