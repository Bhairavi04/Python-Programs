# Write a program to take input from the user and stop when the input is greater than 100.
number=int(input("Enter the number : "))
while (True):
    if (number < 100):
        number = int(input("Enter the number : "))
        continue

    if (number >100):
        print("congrats you have crossed 100!!")
        break