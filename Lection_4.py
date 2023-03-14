# Анонимные, lambda-функции
def f(x):
    return x ** 2
g = f
# Теперь в контексте этого приложения g может использоваться точно так же, как и f.
# g — это переменная, которая хранит в себе ссылку на функцию.
-----------------------
def sum(x, y):
    return x + y
# ⇔ (равносильно)

sum = lambda x, y: x + y
-------------------
# Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.

list_1 = [x for x in range (1,20)]
list_1 = list(map(lambda x: x + 10, list_1 ))

data = list(map(int,input().split()))

# Результат работы map() — это итератор. По итератору можно пробежаться только один раз. Чтобы
# работать несколько раз с одними данными, нужно сохранить данные (например, в виде списка).
----------------------
# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для которых функция вернула True.
data = [x for x in range(10)]
res = list(filter(lambda x: x % 2 == 0, data))
print(res) # [0, 2, 4, 6, 8]
---------------------
# Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами
# из элементов входных данных
# На выходе получаем набор данных, состоящий из элементов соответствующих
# исходному набору.
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]
# Функция zip () пробегает по минимальному входящему набору
----------------------
# Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с
# кортежами из индекса и элементов входных данных.
# Функция enumerate() позволяет пронумеровать набор данных.
users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]
----------------------
# 1. Завести переменную, которая будет связана с этим текстовым файлом.
# 2. Указать путь к файлу.
# 3. Указать, в каком режиме мы будем работать с файлом.

# a – открытие для добавления данных.
# ○ Позволяет дописывать что-то в имеющийся файл.
# ○ Если вы попробуете дописать что-то в несуществующий файл, то файл будет создан
# и в него начнется запись.
colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
data.writelines(colors) # разделителей не будет
data.close()
#  Ещё один способ записи данных в файл:
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')

# r – открытие для чтения данных.
# ○ Позволяет читать данные из файла.
# ○ Если вы попробуете считать данные из файла, которого не существует, программа
# выдаст ошибку.
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

# w – открытие для записи данных.
# ○ Позволяет записывать данные и создавать файл, если его не существует.
colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) # разделителей не будет
data.close()
# ● В итоге создаётся текстовый файл с текстом внутри: ‘redbluedreen’.
# ● В случае перезаписи новые данные записываются, а старые удаляются.

# Миксованные режимы:
# 1. w+
# ○ Позволяет открывать файл для записи и читать из него.
# ○ Если файла не существует, он будет создан.
# 2. r+
# ○ Позволяет открывать файл для чтения и дописывать в него.
# ○ Если файла не существует, программа выдаст ошибку.
---------------------------
import os # сначала импортируем

os.chdir(path) - # смена текущей директории.
os.chdir('C:/Users/79190/PycharmProjects/GB')

os.getcwd() - # текущая рабочая директория
print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject'

os.path - # является вложенным модулем в модуль os и реализует некоторые полезные функции для работы с
# путями, такие как:
os.path.basename(path) - # базовое имя пути
print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py')) #'main.py'

os.path.abspath(path) - # возвращает нормализованный абсолютный путь.
print(os.path.abspath('main.py')) # 'C:/Users/79190/PycharmProjects/webproject/main.py'
