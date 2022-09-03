#!/usr/bin/python3

def multiplyList(myList) :
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result

def weight_average(my_list=[]):
    return sum(list(map(lambda x:multiplyList(x), my_list)))/sum(list( map(lambda y:y[1], my_list) ))
