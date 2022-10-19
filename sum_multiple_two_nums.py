# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))

if a*b <= 1000:
    print("The product is :", a*b)
else:
    print("The sum is :", a+b)
