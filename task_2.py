#2.	Для даного   обчислити значення функції:
# F(x)={ 9, якщо x ≤ -3 ; 1 / ( x^2 + 1 ), якщо x > -3.)


x = int(input("Enter a value for x: "))
if x <= -3:
    print("F(x): 9")
else:
    print("F(x):", 1 / (x ** 2 + 1))
