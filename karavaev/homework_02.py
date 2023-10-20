# Функция для инвертирования списка
def reverse(input_list):
    return input_list[::-1]

# Функция для вычисления средней длины слов в списке
def avglen(word_list):
    if not word_list:
        return 0.0

    total_length = sum(len(word) for word in word_list)
    average_length = total_length / len(word_list)
    return average_length

# Функция для поиска порядковых номеров слов в списке
def index(word_list):
    word_dict = {}
    for index, word in enumerate(word_list):
        if word in word_dict:
            if isinstance(word_dict[word], list):
                word_dict[word].append(index)
            else:
                word_dict[word] = [word_dict[word], index]
        else:
            word_dict[word] = index
    return word_dict

# Функция для нахождения совпадающих элементов в двух списках
def coincidence(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = list(set1.intersection(set2))
    return common_elements

# Функция для подсчета количества повторений слов в списке
def count(word_list):
    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

# Функция для сортировки слов по длине
def lensort(word_list):
    return sorted(word_list, key=lambda x: (len(x), x))

