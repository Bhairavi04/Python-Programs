# Write a function, add_it_up(),
# that takes a single integer as input and returns the sum of the integers from zero to the input parameter.


def add_it_up(a):
    i = 0
    for b in range(0, a+1):
        i = i+b
    print(i)


add_it_up(4)
