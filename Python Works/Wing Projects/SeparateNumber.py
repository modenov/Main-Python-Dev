"""
Последняя цифра: (num // 10**0) % 10;
Предпоследняя цифра: (num // 10**1) % 10;
Предпредпоследняя цифра: (num // 10**2) % 10;
.....
Вторая цифра: (num // 10**(n-2)) % 10;
Первая цифра: (num // 10**(n-1)) % 10.
"""

# программа, в которую вводится трёхзначное число и которая выводит на экран его цифры (через запятую)
num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
print(digit1, digit2, digit3, sep=',')