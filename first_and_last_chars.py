''' Q.
Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''

slist=['abc','xyz','aba','1221']
new_list=[]
for i in slist:
    if i[0]==i[-1]:
        new_list.append(i)
print("Result is",len(new_list))




