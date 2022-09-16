#while loop using continue and break
i=0
while (True):
    if i<5:
        print(i,end=" ")
        i+=1
        continue
    print(i,end=" ")
    i+=1
    if i==45:
        break