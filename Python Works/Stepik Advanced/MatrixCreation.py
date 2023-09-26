#  Copyright (c) Vladimir Modenov.
#  Created: 23.10.2022, 17:08
#  Project: StepikPythonAdvanced
#  File: MatrixCreation.py

N = int(input())
M = int(input())

A = []
for i in range(N):
    A.append([0]*M)

print('Вывод матрицы в строчку:')
print(A)
print('------------')
print('Вывод матрицы в столбик:')
for i in range(len(A)):         # len(A) - возвращает количество строк в матрице А
    for j in range(len(A[i])):  # len(A[i]) - возвращает количество элементов в строке i
        print(A[i][j], end=' ')
    print()
