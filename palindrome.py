__author__ = 'QHe'

'''Find the largest palindrome made from the product of two 3-digit numbers.'''

import math
max_product = 0

'''for i in range(999, 100, -1):
    for t in range(999, 100, -1):
        product = i * t
        digit1 = product % 10
        digit2 = (product % 100) /10
        digit3 = (product % 1000) / 100
        digit4 = (product % 10000) / 1000
        digit5 = (product % 100000) / 10000
        digit6 = (product % 1000000) / 100000
        if product > 99999 and digit6 == digit1 and digit5 == digit2 and digit4 == digit3:
            max_product = max(max_product, product)
        elif product <= 99999 and digit5 == digit1 and digit4 == digit2:
            max_product = max(max_product, product)

print max_product'''

'''Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

sum_sqrs = 0
sqrs_sum = 0

for i in range(1, 101):
    sum_sqrs = sum_sqrs + (i ** 2)
    sqrs_sum = sqrs_sum + i

print sqrs_sum



print abs((sqrs_sum ** 2) - sum_sqrs)

