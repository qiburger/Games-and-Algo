# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 10:48:15 2015

@author: QHe
"""

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

b = 2
a = 600851475143

while b * b <= a:
    while a % b == 0:
        answer = b
        a = a / b
    if a == 1:
        answer = b
    else:
        b = b + 1
if a == 1:
    print answer
else:
    answer = a
    print answer





