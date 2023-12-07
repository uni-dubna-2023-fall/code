def reverse(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst


def avglen(words):
    total_length = 0
    for word in words:
        total_length += len(word)
    average_length = total_length / len(words)
    return average_length


def index(words):
    index_dict = {}
    for i in range(len(words)):
        word = words[i]
        if word in index_dict:
            index_dict[word].append(i)
        else:
            index_dict[word] = (i)
    return index_dict


def count(words):
    counts = {}
    index = 0
    while index < len(words):
        word = words[index]
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
        index += 1
    return counts


def coincidence(list1, list2):
    common_elements = []
    for item1 in list1:
        if item1 in list2 and item1 not in common_elements:
            common_elements.append(item1)
    return common_elements


def lensort(words):
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) > len(words[j]):
                words[i], words[j] = words[j], words[i]
    return words
