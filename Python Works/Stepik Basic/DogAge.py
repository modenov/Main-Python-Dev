"""
На вход программе подается число nnn – количество собачьих лет. Напишите программу, которая вычисляет возраст
собаки в человеческих годах.
На вход программе подаётся натуральное число – количество собачьих лет.
"""

age = int(input())
if age <= 2:
    age = age * 10.5
    print(age)
else:
    age = 21 + (age - 2) * 4
    print(age)