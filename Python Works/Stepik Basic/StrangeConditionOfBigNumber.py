# программа, которая проверяет, что для заданного четырехзначного числа сумма первой и последней цифр равна разности второй и третьей цифр
abcd = int(input())
a = (abcd % 10000) // 1000
b = (abcd % 1000) // 100
c = (abcd % 100) // 10
d = abcd % 10
if (a + d) == (b - c):
    print('ДА')
else:
    print('НЕТ')