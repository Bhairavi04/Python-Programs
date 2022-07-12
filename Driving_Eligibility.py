""" Take age as input from user.Is more than 18 can drive.Is less than 18 cannot drive.
Is 18 than we can't decide now you have to come phisically to visit our office."""

age=int(input("Enter your age to check if you are eligible to drive : "))
if age>18:
    print("You are allowed to drive!!")
elif age==18:
    print("We can't decide now,you have to come physically to visit our office.")
else:
    print("You are not allowed to drive.")
