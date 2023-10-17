#1
def reverse(l):
    new_l = []
    for i in range(1, len(l) + 1):
        new_l.append(l[-i]) 
    return new_l

#2
def avglen(l):
    c=0
    for word in l:
        c=len(word)+c
    return c/len(l)

#3
def index(list):
    word_i={}
    n=len(list)
    for i in range(n):
        word=list[i]
        if word in word_i:
            if type(word_i[word]) is list:
                word_i[word].append(i)
            else:
                word_i[word] = [word_i[word], i]
        else:
            word_i[word] = i
    return word_i

#4
def coincidence(list1,list2):
    newlist=[]
    for i in list1:
        for j in list2:
            if i==j:
                newlist.append(i)
    return newlist
 
#5
def count(list):
    word_i={}
    for i in list:
       if i in word_i:
            word_i[i] += 1
       else:
            word_i[i] = 1
    return word_i

#6
def lensort(list):
    diction = {}
    max_len = 0
    for i in list:
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
 
