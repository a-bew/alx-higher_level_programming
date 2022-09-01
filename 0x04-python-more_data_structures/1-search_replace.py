#!/usr/bin/python3

def search_replace(my_list, search, replace):
    my_list_copy = my_list
    for  i in range(len(my_list)):
        if search == my_list[i]:
            my_list_copy[i] = replace
    return my_list_copy
