

def reverse(lst):
    return lst[::-1]


def avglen(lst):
    if len(lst) == 0:
        return 0
    total_len = sum(len(word) for word in lst)
    return total_len / len(lst)


def index(lst):
    index_dict = {}
    for i, word in enumerate(lst):
        if word in index_dict:
            index_dict[word].append(i)
        else:
<<<<<<< HEAD
            index_dict[word] = [i]
=======
            index_dict[word] = i
>>>>>>> 9c6dcf2 (yakovlev homework 02)
    return index_dict


def coincidence(lst1, lst2):
    return list(set(lst1) & set(lst2))


def count(lst):
    count_dict = {}
    for word in lst:
        count_dict[word] = count_dict.get(word, 0) + 1
    return count_dict


def lensort(lst):
    lst.sort(key=lambda x: len(x))
    return lst
