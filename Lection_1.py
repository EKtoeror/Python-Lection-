# - строчный коммент
"""
многострочный коммент
"""
# ctr+k + ctr+c комментирование выделенного
# ctr+k + ctr+u разкомментирование выделенного

# \ d в строке для печати ковычек внутри строки
# print(type(n)) - указать тип переменной

"""
интерполяция строк  
print(f"{x}{y}{z}")
print("{}{}{}".format(x,y,z))
"""

"""
input()-ввод данных
x = input() - ввод и сохранение в переменной

print("comment") - коммент
x= input() - ввод с новой строки

x = input ("comment") - коммент и ввод в одной строке

"""
# print(x+y) - сложение строк
# x = int(x) - изменение типа данных переменной (float,bool,str)
# x = int(input()) - изменение типа данных при вводе
# // - целочисленное деление
# ** - возведение в степень
# print(round(x*y - число,2 - число знаков после запятой)) - округление чисел

"""
iter = 2
iter += 3 # iter = iter + 3
iter -= 4 # iter = iter - 4
iter *= 5 # iter = iter * 5
iter /= 5 # iter = iter / 5
iter //= 5 # iter = iter // 5
iter %= 5 # iter = iter % 5
iter **= 5 # iter = iter ** 5
"""

"""
r = range(5) # 0 1 2 3 4
r = range(2, 5) # 2 3 4
r = range(-5, 0) # ----
r = range(1, 10, 2) # 1 3 5 7
r = range(100, 0, -20) # 100 80 60 40 20
r = range(100, 0, -20) # range(100, 0, -20)
"""

"""
text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.lower()) # съешь ещё этих мягких французских булок
print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок
"""

"""
text = 'съешь ещё этих мягких французских булок'
 print(text[0]) # c
 print(text[1]) # ъ
 print(text[len(text)-1]) # к
 print(text[-5]) # б
 print(text[:]) # съешь ещё этих мягких французских булок
 print(text[:2]) # съ
 print(text[len(text)-2:]) # ок
 print(text[2:9]) # ешь ещё
 print(text[6:-18]) # ещё этих мягких
 print(text[0:len(text):6]) # сеикакл
 print(text[::6]) # сеикакл
 text = text[2:9] + text[-5] + text[:2] # ...
"""
