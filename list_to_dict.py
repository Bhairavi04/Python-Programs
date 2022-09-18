'''Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from 
list1 is the key and item from list2 is the value'''


# Using zip function

#keys = ['Ten', 'Twenty', 'Thirty']
#values = [10, 20, 30]
#new_dict = dict(zip(keys, values))
# print(new_dict)


# using for loop and update() function
dict1 = {}
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
for i in range(len(keys)):
    dict1.update({keys[i]: values[i]})
print(dict1)
