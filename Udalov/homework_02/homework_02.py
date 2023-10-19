def reverse(list):
    b=[]
    for i in range(len(list)):
        b.append(list-i-1)
    return b

def avglen(list):
    s=0
    for i in list:
        s+=len(i)
    return s/len(list)

def index(list):
    dictionary = {}
    for i in range(len(list)):
        if list[i] not in dictionary:
            dictionary[list[i]]=[i]
        else:
            dictionary[list[i]].append(i)
    return dictionary

def coincidence(list1, list2):
    b=[]
    for i in list1:
        for c in range(len(list2)):
            if (i==list2[c]) and (i not in b):
                b.append(i)
    return b

def count(list):
    dictionary={}
    for i in range(len(list)):
        if list[i] not in dictionary:
            dictionary[list[i]]=1
        else:
            dictionary[list[i]]+=1
    return dictionary

def lensort(list):
    for i in range(len(list)-1):
        for j in range(i,len(list)):
            if len(list[i])>len(list[j]):
                temp = list[i]
                list[i]=list[j]
                list[j]=temp
    return list