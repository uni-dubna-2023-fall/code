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

