#  Copyright (c) Vladimir Modenov.
#  Created: 10.10.2022, 22:37
#  Project: StepikPythonAdvanced
#  File: DivisibilityPredicate.py

# объявление функции
def func(num1, num2):
    return num1 % num2 == 0


# считываем данные
num1, num2 = int(input()), int(input())

# вызываем функцию
if func(num1, num2):
    print('делится')
else:
    print('не делится')
