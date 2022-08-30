#!/usr/bin/python3
def no_c(my_string):
    j = 0
    new_string = my_string[:]
    for i in range(len(my_string)):
        if "c" == my_string[i] or "C" == my_string[i]:
            new_string = new_string[:(i - j)] + my_string[(i + 1):]
            j += 1

    return (new_string)
