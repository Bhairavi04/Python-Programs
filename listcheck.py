#check whether the value is integer and greater than 6

list1=[2,1,"green",6,"hen,",9, 34]
for i in list1:
    if type(i)==int and i>6:
        print("The detected value that is integer and greater than 6 is ", i)