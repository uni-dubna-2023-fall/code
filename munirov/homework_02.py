def reverse(lst):
    return lst[::-1]

def avglen(lst):
    count = 0
    for word in lst:
        count = len(word) + count
    return count / len(lst)


def index(words):
    result = {}
    count = 0 
    for word in words:
        if word in result:
            if isinstance(result[word], int):
                result[word] = [result[word], count]
            else:
                result[word].append(count)
        else:
            result[word] = count
        count += 1
    return result


def coincidence(lst1, lst2):
    return list(set(lst1) & set(lst2))


def count(lst):
    result = {}
    for word in lst:
        result[word] = result.get(word, 0) + 1
    return result


def lensort(lst):
    return sorted(lst, key=len)


arg = ["my", "name", "is", "Masha"]
print(reverse(arg))  # ["Masha", "is", "name", "my"]

arg = ["a", "ab", "abc"]
print(avglen(arg))  # 2.0

arg = ["her", "name", "is", "Masha", "Masha", "is", "a", "sister", "of", "Zhenya"]
print(index(arg))
# {
#     "her": 0,
#     "name": 1,
#     "is": [2, 5],
#     "Masha": [3, 4],
#     "a": 6,
#     "sister": 7,
#     "of": 8,
#     "Zhenya": 9,
# }

arg1 = ["my", "name", "is", "Masha"]
arg2 = ["my", "name", "is", "Zhenya"]
print(coincidence(arg1, arg2))  # ["my", "name", "is"]

arg = ["aaa", "aaa", "bbb", "ccc", "bbb"]
print(count(arg))
# {
#     "aaa": 2,
#     "bbb": 2,
#     "ccc": 1,
# }

arg = ["abcd", "a", "ab", "abc", "bazinga", "bar"]
print(lensort(arg))  # ["a", "ab", "abc", "bar", "abcd", "bazinga"]
