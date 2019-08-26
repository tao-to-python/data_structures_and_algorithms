# -*- coding:utf-8 -*-
number_list = list(range(8))

def linear_search(value,iterable):
    for index,val in enumerate(iterable):
        if val==value:
            return index 
    return -1

def linear_search_v2(predicate,iterable):
    for index,val in enumerate(iterable):
        if predicate(val):
            return index
    return -1

def linear_search_recursive(array,value):
    if len(array) == 0:
        return -1
    index = len(array)-1
    if array[index] == value:
        return index
    return linear_search_recursive(array[:index],value)

def binary_search_recursive(sorted_array,beg,end,val):
    if beg >= end:
        return -1
    
    mid = int((beg+end)/2) 
    if sorted_array[mid] == val:
        return mid
    elif sorted_array[mid] > val:
        return binary_search_recursive(sorted_array,beg,mid,val)
    else:
        return binary_search_recursive(sorted_array,mid,end,val)
    
    
def test_binary_search_recursive():
    a = list(range(10))
    for i in a :
        assert binary_search_recursive(a,0,len(a),i) == i