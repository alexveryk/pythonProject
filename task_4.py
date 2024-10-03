'''
3. Дано число k. Напишіть програму, яка виводить суму найменшого і найбільшого елементу
із послідовності чисел Фібоначчі із k елементів
'''

k = int(input("Enter the number of items in the list "))
fib_sequence = []
for i in range(k):
    if i <= 1:
        fib_sequence.append(i)
    if i > 1:
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

min_num = fib_sequence[0]
max_num = fib_sequence[-1]

print(fib_sequence)
print(f"The largest number - {max_num}, ", f"is the smallest - {min_num}, ", f"sum of numbers - {min_num + max_num}", )



