# -*- coding:utf-8 -*-

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot_index = 0
        pivot = array[pivot_index]
        # 缺点：1、需要额外的存储空间；2、partition操作每次均需要两次遍历整个数组
        less_part = [i for i in array[pivot_index+1:] if i <= pivot]
        great_part = [i for i in array[pivot_index+1:] if i > pivot]
        return quicksort(less_part)+[pivot]+quicksort(great_part)
    
    
#一次遍历实现partition
def partition(array,beg,end):
    pivot_index = 0
    pivot = array[pivot_index]
    
    left = pivot_index+1
    right = end -1
    
    while True:
        while left <= right and array[left] < pivot:
            left += 1
        
        while right >= left and array[right] >= pivot:
            right -= 1
        
        if left > right:
            break
        else:
            array[left],array[right] = array[right],array[left]
    #交换主元和right的值
    array[pivot_index],array[right] = array[right],array[pivot_index]
    return right

# def test_partition():
#     l = [4,1,2,8]
#     assert partition(l,0,len(l)) == 2
#     l = [1,2,3,4]
#     assert partition(l,0,len(l)) == 0
    
def quicksort_inplace(array,beg,end):
    if beg < end:
        pivot = partition(array,beg,end) 
        quicksort_inplace(array,beg,pivot)
        quicksort_inplace(array,pivot+1,end)   
    
    
# def test_quicksort():
#     import random
#     seq = list(range(10))
#     random.shuffle(seq)
#     assert quicksort(seq) == sorted(seq)

def test_quicksort_inplace():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    print(seq)
    # assert quicksort_inplace(seq,0,len(seq)) == sorted(seq)
    quicksort_inplace(seq,0,len(seq))
    print(seq)