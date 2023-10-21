def reverse(list1):
    new_l = []
    for i in range(1, len(list1) + 1):
        new_l.append(list1[-i]) 
    return new_l


def avglen(list1):
    c=0
    for word in list1:
        c=len(word)+c
    return c/len(list1)


def index(list1):
    word_i={}
    n=len(list1)
    for i in range(n):
        word=list1[i]
        if word in word_i:
            if type(word_i[word]) is list1:
                word_i[word].append(i)
            else:
                word_i[word] = [word_i[word], i]
        else:
            word_i[word] = i
    return word_i


def coincidence(list1,list2):
    newlist=[]
    for i in list1:
        for j in list2:
            if i==j:
                newlist.append(i)
    return newlist


def count(list1):
    word_i={}
    for i in list1:
       if i in word_i:
            word_i[i] += 1
       else:
            word_i[i] = 1
    return word_i


def lensort(list1):
    diction = {}
    max_len = 0
    for i in list1:
        n = len(i)
        if n in diction:
            diction[n].append(i)
        else:
            diction[n] = [i]
        max_len = max(max_len, n)
    sort_list = []
    for i in range(max_len+1):
        if i in diction:
            sort_list.extend(diction[i])
    return sort_list
    
