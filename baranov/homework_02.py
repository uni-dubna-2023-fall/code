

def reverse(word):
    new_word = []
    for i in range(1, len(word) + 1):
        new_word.append(word[-i])
    return new_word


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


def lensort(words):
    word_lengths = {}
    for word in words:
        length = len(word)
        if length in word_lengths:
            word_lengths[length].append(word)
        else:
            word_lengths[length] = [word]
    sorted_words = []
    for length in sorted(word_lengths.keys()):
        sorted_words.extend(word_lengths[length])
    return sorted_words
