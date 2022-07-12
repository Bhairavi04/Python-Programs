#Create a list of fruits and how much are they available.Print the fruits that are more than 6.
list1=[["Plums",1],["Apples",7],["Bananas",9],["Oranges",2]]
for item,number in list1:
    if number > 6:
        print(item,number)