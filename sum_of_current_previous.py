# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
n = int(input("Enter the number :"))
for i in range(n):
    print("Current number :", i, "Previous number :", i-1, "Sum :", i+(i-1))
