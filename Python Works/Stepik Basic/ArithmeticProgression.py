"""
Программа, определяющая, являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии
"""

a = int(input())
b = int(input())
c = int(input())
if (b - a) + b == c:
    print("YES")
else:
    print("NO")
