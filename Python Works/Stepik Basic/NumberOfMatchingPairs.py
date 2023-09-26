#  Copyright (c) Vladimir Modenov.
#  Created: 20.09.2022, 22:55
#  Project: StepikPythonProjects
#  File: NumberOfMatchingPairs.py

# На вход программе подается строка текста, содержащая натуральные числа. Из данной строки формируется список чисел.
# Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу. Считается,
# что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

a = input().split()
s = 0

for i in range(len(a) - 1):
    s += a[i + 1:].count(a[i])

print(s)
