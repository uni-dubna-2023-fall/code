def reverse(array):
    return array[::-1]


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
    return list(set(array1).intersection(array2))


def count(array):
    dictionary = {}
    for word in array:
        dictionary[word] = dictionary.get(word, 0) + 1
    return dictionary


def lensort(words):
    n = len(words)

    for i in range(1, n):
        current_word = words[i]
        j = i - 1

        while j >= 0 and len(current_word) < len(words[j]):
            words[j + 1] = words[j]
            j -= 1

        words[j + 1] = current_word

    return words