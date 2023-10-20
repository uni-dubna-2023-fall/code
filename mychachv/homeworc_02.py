lst= ["her", "name", "is", "Masha", "Masha", "Masha", "is", "a", "sister", "of", "Zhenya"]
lst1=["a","b","c","d"]
lst2=["a","b","c","f"]

def reverse(lst):
   return lst[::-1]
#срез с отрицательным значением шага, [start:stop:step], параметр `step` указывает шаг, с которым происходит итерация по элементам. Если значение `step` равно `-1`, то итерация происходит в обратном порядке.

def avglen(lst):
    c = 0
    for word in lst:
        c = len(word) + c
    return c / len(lst)

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
# `set` в Python является встроенным типом данных, представляющим неупорядоченную коллекцию уникальных элементов.
# здесь применяется алгебра логики (логическое "и" или конъюнкция) где 10110 & 10011 = 10010

def count(lst):
    word_count = {}
    for word in lst:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def lensort(lst):
    upper = []
    lower = []
    
    for string in lst:
        if string[0].isupper():
            upper.append(string)
        else:
            lower.append(string)
    
    upper.sort()
    lower.sort()
    
    return upper + lower

print(reverse(lst))
print(avglen(lst))
print(index(lst))
print(coincidence(lst1, lst2))
print(count(lst))
print(lensort(lst))