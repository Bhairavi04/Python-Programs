# Create a function in such a way that we can pass any number of
# arguments to this function and the function should process them and display how many arguments were passed.

def argument_length(*vars):
    value = len(vars)
    print(value, "arguments were passed")


argument_length("a", "b", "c", "d")
