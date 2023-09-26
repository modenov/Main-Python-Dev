"""
Последняя цифра: (num // 10**0) % 10;
Предпоследняя цифра: (num // 10**1) % 10;
Предпредпоследняя цифра: (num // 10**2) % 10;
.....
Вторая цифра: (num // 10**(n-2)) % 10;
Первая цифра: (num // 10**(n-1)) % 10.
"""

# сумма сложения цифр двузначного числа
num = int(input())
last_digit = num % 10
first_digit = num // 10
print('Сумма цифр =', last_digit + first_digit)