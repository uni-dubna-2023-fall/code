# Основы Python

## Основные типы данных в Python
- Целые числа `int`
- Числа с плавающей точкой `float`
- Строки `str`
- Истина/ложь `bool`

```python
>>> type(1)
<type 'int'>
>>> type(1.0)
<type 'float'>
>>> type('1')
<type 'str'>
>>> type(True)
<type 'bool'>
>>>
```

## Переменные в Python
```python
a = "Hello, "
b = "world!"
print(a + b)
Hello, world!
```

## Основные структуры данных в Python
- Список `list`
- Словарь `dict`
- Кортеж `tuple` (похоже на список, но только нельзя менять)
- Множество `set` (похоже на список, повторяющиеся элементы считаются одним и тем же элементом)

```python
>>> a = [1, 1.0, 'something', True]
>>> b = {"key1": "value1", "key2": "value2"}
>>> c = ("hello", "world")
>>> d = {"foo", 1}
>>> type(a)
<class 'list'>
>>> type(b)
<class 'dict'>
>>> type(c)
<class 'tuple'>
>>> type(d)
<class 'set'>
```

## Основные операции со списками
```python
>>> a = [1, 1.0, "something", True]
>>> len(a)
4
>>> a.append(10)
>>> a
[1, 1.0, 'something', True, 10]
>>> len(a)
5
>>> a[0]
1
>>> a[2]
'something'
>>> a[2:]
['something', True, 10]
>>> a[2:4]
['something', True]
>>> for element in a:
        print(element)
```

## Основные операции со словарями
```python
>>> b = {"key1": "value1", "key2": "value2"}
>>> b.keys()
['key2', 'key1']
>>> b.values()
['value2', 'value1']
>>> len(b)
2
>>> b['key3'] = 'value3'
>>> b['key2']
'value2'
>>> b
{'key3': 'value3', 'key2': 'value2', 'key1': 'value1'}
del b['key1']
>>> b
{'key3': 'value3', 'key2': 'value2'}
>>> for k in b:
        print(f"{k}: {b[k]}")
```

## Основные операции с множествами
>>> d = {1}
>>> d
{1}
>>> d.add(2)
>>> d
{1, 2}
>>> len(d)
2
>>> d.remove(1)
>>> d
{2}
>>> e = {4, 5}
>>> d.union(e)
{2, 4, 5}
>>> d.intersection(e)
set()

## Условия в Python
Можно так
```python
a = 5
if a < 10:
    print("a is less than 10")
else:
    print("a is more that 10 or equal to 10")
```

Или так
```python
name = "Jack"
if name == "Petya":
    print("Hello, Petya")
elif name == "Vasya":
    print("Hello, Vasya")
else:
    print("What is your name?")
```

## Циклы в Python
Цикл `for`
```python
for i in range(5):
    print(i)
```

Цикл `while`
```python
i = 5
while i > 0:
    print(i)
    i = i - 1
```

Итерироваться можно по списку
```python
l = ["Ivan", "Maria", "David"]
for name in l:
    print(name)
```

Выполнение цикла можно прервать при помощи `break`
```python
for i in range(10):
    print(i)
    if i > 3:
        break
```

## Функции в Python
```python
def func(arg1, arg2):
    print("Hello, I am func and I am going to return a list")
    return [arg1, arg2]
a = func(1, 2)
b = func("hello", "world")
```

## Классы в Python
```python
class Animal:
    def __init__(self, weight):
        self._weight = weight

    def say(self):
        print("Can not say anything")

    def weight(self)
        print(self._weight)

class Cat(Animal):
    def say(self):
        print("Meow")

class Dog(Animal):
    def say(self):
        print("Woof")

a = Animal(1)
a.say()
a.weight()
c = Cat(5)
c.say()
c.weight()
d = Dog(10)
d.say()
d.weight()
```
