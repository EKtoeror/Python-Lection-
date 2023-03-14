# def function_name(x):
# body line 1
# ...
# body line n
# optional return

def sum_numbers1(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)


sum_numbers1(5)
#  2 пустых строки перед вызовом функции


#  2 пустых строки перед объявлением новой функции
def sumNumbers2(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa


print(sumNumbers2(1))

# def sum_numbers1(*args): - бесконечное число аргутментов

# Модульнойсть:
# 1. Создаем новый файл питона
# 2. Прописываем там функции
# Чтобы вызвать в рабочем файле:

# import "название модуля" ("as другое название")
# print(Эназвание модуля.название функции:(аргументы))
# или
# from "название модуля" import "название функции" ("*" все функции)
# print("название функции(аргументы)")


#  Последовательность Фибоначи через рекурсию
def fib(n):
    if n in [1, 2]:  # Базис рекурсии
        return 1
    return fib(n - 1) + fib(n - 2)


list_1 = []
for i in range(1, 10):
    list_1.append(fib(i - 2))
print(list_1)  # [1, 1, 2, 3, 5, 8, 13, 21, 34]


# Быстрая сортировка
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))
