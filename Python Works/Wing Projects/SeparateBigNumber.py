"""
Последняя цифра: (num // 10**0) % 10;
Предпоследняя цифра: (num // 10**1) % 10;
Предпредпоследняя цифра: (num // 10**2) % 10;
.....
Вторая цифра: (num // 10**(n-2)) % 10;
Первая цифра: (num // 10**(n-1)) % 10.
"""

# Разделяем 4х-значое число
num = int(input())
digit4 = (num // 10**0) % 10
digit3 = (num // 10**1) % 10
digit2 = (num // 10**2) % 10
digit1 = (num // 10**3) % 10
print(f"Цифра в позиции тысяч равна {digit1}")
print(f"Цифра в позиции сотен равна {digit2}")
print(f"Цифра в позиции десятков равна {digit3}")
print(f"Цифра в позиции единиц равна {digit4}")

# not my code
m = int(input())
m1 = m // 1000
m2 = (m // 100) % 10
m3 = (m // 10) % 10
m4 = m % 10
print("Цифра в позиции тысяч равна", m1)
print("Цифра в позиции сотен равна", m2)
print("Цифра в позиции десятков равна", m3)
print("Цифра в позиции единиц равна", m4)