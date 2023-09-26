# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
res = 0
for num in numbers:
    res += (num % 2 == 1) and (num > 1)
print(res)

print(True + 1)


numbers = [10, 20, 30, 40, 50]
print(numbers[-2])
print(numbers[-4:-1])


numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[2:5])
print(numbers[:4])
print(numbers[3:])


numbers = [4, 8, 12, 16, 34, 56, 100]
numbers[1:4] = [20, 24, 28]
print(numbers)

numbers = [5, 10, 15, 25]
print(numbers[::-2])
