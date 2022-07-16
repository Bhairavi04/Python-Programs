#iterate through the list and if there is a 100, print it with its index number. i.e.: "There is a 100 at index no: 5"
list1=[12,15,25,78,10,100,45]
for item in list1:
	if item==100:
		print("There is a 100 at index no:",list1.index(100))