# To check whether the last digit of a number( entered by user ) is divisible by 3 or not.

number = int(input("Enter a number :"))
last_digit = number % 10  # To get the last digit of the number entered by users
if last_digit % 3 == 0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")
