"""
Завдання на масиви, розмір масиву і масив зчитувати із консолі.

3. Задано масив із  n елементів.
Вивести на екран лише парні елементи масиву. У звіті продемонструвати результат на
масиві який складається із парних та не парних елементів.
"""

n = int(input('Задайте довжину масива: '))
arr = []
even_numbers = []

for i in range(n):
    x = int(input("Введи число => "))
    arr.append(x)
print("Ваш список: ",arr)

for item in arr:
    if item % 2  == 0:
        even_numbers.append(item)

print("Парні:", even_numbers)


