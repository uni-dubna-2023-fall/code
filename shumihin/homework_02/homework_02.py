def reverse(array):
    result = []
    for obj in array:
        result.insert(0, obj)
    return result


def avglen(array):
    total_letters = 0
    for word in array:
        total_letters += len(word)
    return total_letters / len(array)


def index(array):
    dictionary = {}
    for value, key in enumerate(array):
        if key not in dictionary.keys():
            dictionary[key] = [value]
        else:
            dictionary[key].append(value)
    for key in dictionary.keys():
        if len(dictionary[key]) == 1:
            copy = dictionary[key][0]
            dictionary[key] = copy
    return dictionary


def coincidence(array1, array2):
    result = []
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                result.append(array1[i])
    return result


def count(array):
    dictionary = {}
    for word in array:
        if word not in dictionary.keys():
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    return dictionary


def lensort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if len(array[j]) > len(array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
    return array