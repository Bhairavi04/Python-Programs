#Create a dictionary and take input from the user and return meaning of the word from the dictionary
key=input("Enter the word to get the meaning : ")
dict={"excite":"cause (someone) to feel very enthusiastic and eager","astonish":"greatly surprised or impressed","compliance":"the action or fact of complying with a wish or command","endeavour":"try hard to do or achieve something","prejudice":"try hard to do or achieve something "}
if key=="excite":
    print("meaning : ",dict["excite"])
elif key=="astonish":
    print("meaning : ",dict["astonish"])
elif key=="compliance":
    print("meaning : ",dict["compliance"])
elif key=="endeavour":
    print("meaning : ",dict["endeavour"])
elif key=="prejudice":
    print("meaning : ",dict["prejudice"])
else:
    print("Sorry,this word is not listed in the dictionary")