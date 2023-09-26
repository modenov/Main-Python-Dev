#  Copyright (c) Vladimir Modenov.
#  Created: 18.09.2022, 17:14
#  Project: StepikPythonProjects
#  File: GoogleSearch2.py

# На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов,
# затем k строк — поисковые запросы. Напишите программу, которая выводит все введенные строки, в которых встречаются
# все поисковые запросы.

s = []  # объявляем основной список
p = []  # объявляем поисковый список

for _ in range(int(input())):  # количество элементов основного списка
    s.append(input())  # добавляем элементы

for _ in range(int(input())):  # количество элементов поискового списка
    p.append(input())  # добавляем элементы

for i in s:  # Ищем для каждого элемента основного списка
    n = 0  # счётчик совпадений
    for k in p:  # сравниваем наличией элемента из списка поиска с основным
        if k.lower() in i.lower():  # если совпадение найдено:
            n += 1  # счётчик прибавляет значение
    if n >= len(
            p):  # если счётчик совпадений равен или больше количеству элементов поискового списка, печатаем элемент
        # из основного списка.
        print(i)
