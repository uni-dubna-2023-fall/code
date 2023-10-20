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

arg1 = ["my", "name", "is", "Masha"]
arg2 = ["my", "name", "is", "Zhenya"]
arg_count = ["aaa", "aaa", "bbb", "ccc", "bbb"]
arg_index = ["her", "name", "is", "Masha", "Masha", "is", "a", "sister", "of", "Zhenya"]
arg_lensort = ["abcd", "a", "ab", "abc", "bazinga", "bar"]

result_reverse = reverse(arg1)
result_avglen = avglen(arg2)
result_index = index(arg_index)
result_coincidence = coincidence(arg1, arg2)
result_count = count(arg_count)
result_lensort = lensort(arg_lensort)

print(result_reverse)
print(result_avglen)
print(result_index)
print(result_coincidence)
print(result_count)
print(result_lensort)
