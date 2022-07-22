# Check if the number entered is a prime number or not using for loop.
num = int(input("enter a number :"))
if num < 0:
    print("Prime numbers cannot be negative")
else:
    for i in range(2, num):
        if num % i == 0:
            print("It is not a prime number")
        else:
            print("It is a prime number")
        break
