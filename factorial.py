# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 10:48:15 2015

@author: QHe
"""

import math

def factorecurse(n):
    if isinstance(n, (int, long)):
        if n == 0:
            return 1
        else:
            return n * factorecurse(n-1)
    else:
        return False

def factoriterate(n):
    total = n
    while n > 1:
        n = n - 1
        total = total * n
    return total

print factorecurse(3)
print factoriterate(3)

