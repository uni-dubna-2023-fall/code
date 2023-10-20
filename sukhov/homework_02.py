from collections import Counter

def reverse(lst):
    return lst[::-1]

def avglen(words):
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

def index(words):
    word_index = {}
    for index, word in enumerate(words):
        if word in word_index:
            if isinstance(word_index[word], list):
                word_index[word].append(index)
            else:
                word_index[word] = [word_index[word], index]
        else:
            word_index[word] = index
    return word_index

def coincidence(lst1, lst2):
    set1 = set(lst1)
    return [x for x in lst2 if x in set1]

def count(words):
    word_count = Counter(words)
    return dict(word_count)

def lensort(words):
    return sorted(words, key=len)
