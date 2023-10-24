

def reverse(source):
    new_source = []
    for i in range(1, len(source) + 1):
        new_source.append(source[-i])
    return new_source


def avglen(array):
    if array:
        total_letters = sum(len(word) for word in array)
        return total_letters / len(array)
    else:
        return 0


def index(array):
    dictionary = {}
    for index, value in enumerate(array):
        if value not in dictionary:
            dictionary[value] = index
        else:
            if isinstance(dictionary[value], list):
                dictionary[value].append(index)
            else:
                dictionary[value] = [dictionary[value], index]
    return dictionary

def coincidence(array1, array2):
    result = []
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                result.append(array1[i])
    return result

def count(lst):
    result = {}
    for word in lst:
        result[word] = result.get(word, 0) + 1
    return result

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
    for i in range(max_len + 1):
        if i in diction:
            sort_list.extend(diction[i])
    return sort_list
