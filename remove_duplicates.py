# Remove duplicate characters from the string
string_new = "abbc"
list_new = list(string_new)
set_new = set(list_new)
back_to_string = repr(set_new)
print(back_to_string)
#print(type(back_to_string))
