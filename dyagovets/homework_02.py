

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


def coincidence(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result


def count(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


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
