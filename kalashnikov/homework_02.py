def reverse(lst):
    return lst[::-1]


def avglen(words):
    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)
    return average_length


def index(words):
    index_dict = {}
    for i, word in enumerate(words):
        if word in index_dict:
            index_dict[word].append(i)
        else:
            index_dict[word] = [i]
    return index_dict


def coincidence(list1, list2):
    return list(set(list1) & set(list2))


def lensort(words):
    return sorted(words, key=len)
