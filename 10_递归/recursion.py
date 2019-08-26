# -*- coding:utf-8 -*-

def fact(n):
    if n == 0:
        return 1
    else:
        n*fact(n-1)
        

def print_num_recursion(n):
    while n > 0:
        print_num_recursion(n-1)
        print(n)
        
def print_num_recursion_reverse(n):
    while n > 0:
        print(n)
        print_num_recursion_reverse(n-1)
        

from collections import deque

class Stack(object):
    def __init__(self):
        self._deque = deque()
        
    def push(self,value):
        return self._deque.append(value)
    
    def pop(self):
        return self._deque.pop()
    
    def is_empty(self):
        return len(self._deque)==0
    
def print_num_use_stack(n):
    s = Stack()
    while n > 0:
        s.push(n)
        n -= 1
        
    while not s.is_empty():
        print(s.pop())
        
def hanoi_move(n,source,dest,intermediate):
    if n >= 1:
        hanoi_move(n-1,source,intermediate,dest)
        print('Move %s ->  %s' %(source,dest))
        hanoi_move(n-1,intermediate,dest,source)
