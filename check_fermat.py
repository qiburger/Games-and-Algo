# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 10:48:15 2015

@author: QHe
"""

import math

def fibonacci(n):
    if isinstance(n, (int, long)):
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return fibonacci(n-2) + fibonacci(n-1)
    else:
        return False

def fib_iter(n):
    total = n
    while n > 1:
        n = n - 1
        total = total * n
    return total

print fibonacci(2)



