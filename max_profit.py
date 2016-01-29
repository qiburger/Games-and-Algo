# coding=utf-8
"""
I have an array called SP of length n which contains a single day’s stock prices
for a single share for Cisco

Write an efficient algorithm for computing the best profit I could have made that day
by buying a single share at a certain time and selling that same share at a certain time.
You must buy before you sell.

Classic max profit problem
"""


def max_profit(array):
    """
    :type array: list of stock prices (float)
    """
    if len(array) < 1:
        return 0
    min_price = array[0]
    profit = 0

    for price in array:
        min_price = min(price, min_price)
        profit = max(profit, price - min_price)

    return profit


print max_profit([4, 4, 5, 7, 3, 1, 8, 4, 9, 0])
