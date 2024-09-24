#1. Дано 4 числа a, b, c, d. Знайти max{min(a,b),min(c,d) }.

print("To find the larger number from two pairs of smaller numbers, enter four numbers")

num_a = int(input("Enter the first number a: "))
num_b = int(input("Enter the second number b: "))
num_c = int(input("Enter the third number с: "))
num_d = int(input("Enter the fourth number b: "))

max_of_min = max(min(num_a,num_b), min(num_c,num_d ))



print("There is a maximum of the minimum:", max_of_min)


