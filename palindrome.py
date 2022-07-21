# Check whether a number is a palindrome number.
number = 151
temp = number
rev = 0
while number > 0:
    last_digit = number % 10
    rev = rev*10+last_digit
    number = number//10

if rev == temp:
    print("number is palindrome")
else:
    print("number is not palindrome")
