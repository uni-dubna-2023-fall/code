def reverse(array):
    reversed_array = []
    for item in array:
        reversed_array.insert(0, item)
    return reversed_array


def avglen(array):
    if not array:
        return 0
    total_length = 0
    count = 0
    for word in array:
        total_length += len(word)
        count += 1
    return total_length / count


def index(array):
    index_dict = {}
    for i in range(len(array)):
        word = array[i]
        if word not in index_dict:
            index_dict[word] = i
        else:
            if isinstance(index_dict[word], list):
                index_dict[word].append(i)
            else:
                index_dict[word] = [index_dict[word], i]
    return index_dict


def coincidence(array1, array2):
    result = []
    for item1 in array1:
        for item2 in array2:
            if item1 == item2 and item1 not in result:
                result.append(item1)
    return result


def count(array):
    word_count = {}
    for word in array:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count


def lensort(array):
    for i in range(len(array) - 1):
        for j in range(i, len(array)):
            if len(array[i]) > len(array[j]):
                array[i], array[j] = array[j], array[i]
    return array
