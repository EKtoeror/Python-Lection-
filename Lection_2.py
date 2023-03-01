list_1 = []  # Создание пустого списка
list_2 = list()  # Создание пустого списка
list_1 = [7, 9, 11, 13, 15, 17]
print(*list_1)  # Вывод результата без скобок

for i in list_1:
    print(i)  # Вывод списка построчно

len  # размер списка
-i  # индекс с конца

list_1.append(n)  # добавление в конец


# Вывод элементов списка
list_1 = [7, 9, 11, 13, 15, 17]
print(list_1[0])  # 7

# Метод pop удаляет последний элемент из списка:
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop())  # 0
print(list_1)  # [12, 7, -1, 21]
print(list_1.pop())  # 21
print(list_1)  # [12, 7, -1]
print(list_1.pop())  # -1
print(list_1)  # [12, 7]

# Удаление конкретного элемента из списка.
# Надо указать значение индекса в качестве аргумента функции pop:
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0))  # 12
print(list_1)  # [7, -1, 21, 0]

# Добавление элемента на нужную позицию.
#  Функция insert — указание индекса (позиции) и значения.
list_1 = [12, 7, -1, 21, 0]
print(list1.insert(2, 11))
print(list1) # [12, 7, 11, -1, 21, 0]

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0])  # 1
print(list_1[1])  # 2
print(list_1[len(list_1)-1])  # 10
print(list_1[-5])  # 6
print(list_1[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2])  # [1, 2]
print(list_1[len(list_1)-2:])  #[9, 10]
print(list_1[2:9])  # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18]) # []
print(list_1[0:len(list_1):6(шаг)])  # [1, 7]
print(list_1[::6])  # [1, 7]

t = ()  # создание пустого кортежа
print(type(t))  # class <'tuple'>
t = (1,)

# Можно распаковать кортеж в независимые переменные:
t = tuple(['red', 'green', 'blue'])
red, green, blue = t

# Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
# В списках в качестве ключа используется индекс элемента. В словаре для определения
# элемента используется значение ключа (строка, число).
dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ← типы ключей могут отличаться
print(dictionary['up']) # ↑ типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
del dictionary['left'] # удаление элемента

for item in dictionary:
    print("{}: {}".format(item.dictionary[item]))

# Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
# Одно множество может содержать значения любых типов. Если у Вас есть два множества,
# Вы можете совершать над ними любые стандартные операции, например, объединение,
# пересечение и разность. Давайте разберем их.
colors = {'red', 'green', 'blue'}  # (q=set())
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok - проверяет и удаляет если есть

# Операции со множествами в Python:
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}

# Неизменяемое или замороженное множество(frozenset) — множество, с которым не будут
# работать методы удаления и добавления.
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})

# Создать список чисел от 1 до 100
list_1 = []
for i in range(1, 101):
list_1.append(i)
print(list_1) # [1, 2, 3,..., 100]
# Эту же функцию можно записать так:
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]

# Добавить условие (только чётные числа)
list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100]
# Допустим, вы решили создать пары каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]
# Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]
