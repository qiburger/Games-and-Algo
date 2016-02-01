import random

import numpy as np
import statistics as statistics


def qselect(array, target_index):
    if len(array) == 1:
        return array[0]

    if len(array) == 2:
        if target_index == 0:
            return min(array[0], array[1])
        elif target_index == 1:
            return max(array[0], array[1])
        else:
            raise ValueError

    pivot_index = random.randint(0, len(array) - 1)

    pivot = array[pivot_index]
    array[pivot_index] = array[-1]
    array[-1] = pivot

    ptr_left = 0
    ptr_right = len(array) - 2

    while True:
        while array[ptr_left] < pivot and ptr_left < (len(array) - 1):
            ptr_left += 1
        while array[ptr_right] >= pivot and ptr_right >= 0:
            ptr_right -= 1
        if ptr_left >= ptr_right:
            break
        else:
            temp = array[ptr_left]
            array[ptr_left] = array[ptr_right]
            array[ptr_right] = temp

    if ptr_left > target_index:
        return qselect(array[:ptr_left], target_index)
    elif target_index > (ptr_right + 1):
        return qselect(array[ptr_left:len(array)], target_index - ptr_left)
    else:
        return pivot


def test_odd_array():
    for i in range(11, 100, 2):

        x = random.sample(range(1, 8), 7)
        y = np.random.choice(i, i, replace=False)

        med = np.median(y)
        q_ans = qselect(y, len(y) / 2)

        if q_ans != med:
            print y
            print med
            print q_ans
            break


test_odd_array()