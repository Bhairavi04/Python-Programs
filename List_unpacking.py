# Create a list and print only the integer and the integer should be greater than 9.
list1=["Team",23,28,6,5,"rabbit,56"]
for numbers in list1:
    if str(numbers).isnumeric() and numbers >9: #isnumeric() checks if the string is in numeric form
        print(numbers)
