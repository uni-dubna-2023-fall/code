def reverse(lst):
    return lst[::-1]


arg = ["my", "name", "is", "Masha"]
result = reverse(arg)
print("1)", result, "\n")



def avglen(words):
    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)
    return average_length


arg = ["a", "ab", "abc"]
result = avglen(arg)
print("2)", result, "\n")



def index(words):
    index_dict = {}
    for i, word in enumerate(words):
        if word in index_dict:
            index_dict[word].append(i)
        else:
            index_dict[word] = [i]
    return index_dict


arg = ["her", "name", "is", "Masha", "Masha", 
       "is", "a", "sister", "of", "Zhenya"]
result = index(arg)
print("3)")
for word, indexes in result.items():
    print(f"{word}: {indexes}")
print("\n")



def coincidence(list1, list2):
    return list(set(list1) & set(list2))


arg1 = ["my", "name", "is", "Masha"]
arg2 = ["my", "name", "is", "Zhenya"]
result = coincidence(arg1, arg2)
print("4)", result, "\n")



def count(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


arg = ["aaa", "aaa", "bbb", "ccc", "bbb"]
result = count(arg)
print("5)", result, "\n")



def lensort(words):
    return sorted(words, key=len)


arg = ["abcd", "a", "ab", "abc", "bazinga", "bar"]
result = lensort(arg)
print("6)", result, "\n")
