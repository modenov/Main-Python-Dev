# Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.
# На вход программе подаются три числа – длины сторон существующего треугольника.

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Равносторонний')
elif a == b or a == c or b == c:
    print('Равнобедренный')
else:
    print('Разносторонний')