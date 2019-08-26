# -*- coding:utf-8 -*-

def merge_sort(seq):
    if len(seq) == 1:
        return seq
    else:
        mid = int(len(seq)/2)
        left_half = merge_sort(seq[:mid])
        right_half = merge_sort(seq[mid:])
        
    # 合并两个有序数组
        new_seq = merge_sort_list(left_half,right_half)
        return new_seq
    
def merge_sort_list(sorted_a,sorted_b):
    length_a ,length_b = len(sorted_a),len(sorted_b)
    a = b = 0
    new_sorted_list = list()
    
    while a < length_a and b < length_b:
        if sorted_a[a] < sorted_b[b]:
            new_sorted_list.append(sorted_a[a])
            a += 1
        else:
            new_sorted_list.append(sorted_b[b])
            b += 1
    
    while a < length_a:
        new_sorted_list.append(sorted_a[a])
        a += 1
        
    while b < length_b:
        new_sorted_list.append(sorted_b[b])
        b += 1
    
    return new_sorted_list


def test_merge_sort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    assert merge_sort(seq) == sorted(seq)
        