"""
    Measure and plot the average time for quicksort
"""
import random

import math
import numpy as np
import timeit
import matplotlib.pyplot as plt


def sort(arr):
    """
    Method from online - the goal of this focuses on timing functions instead of qs
    """
    less = []
    pivot_list = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivot_list.append(i)
        less = sort(less)
        more = sort(more)
        return less + pivot_list + more


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped


def qs_time():
    time_output = {}
    array_size_range = range(500, 700, 1)

    for i in array_size_range:
        test_array = np.random.choice((i * i), i, replace=False)
        test_array = sort(test_array)

        wrapped = wrapper(sort, test_array)
        secs = timeit.timeit(wrapped, number=1)

        time_output[i] = secs

        print secs

    plt.figure(1)
    plt.subplot(121)
    plt.plot(time_output.keys(), time_output.values())
    plt.axis([500, 700, 0.03, 0.12])
    plt.title('Quicksort Time vs Array Size')
    plt.grid(True)

    n_logn = [(i * math.log(i, 2) / 100000) for i in array_size_range]
    n_sqr = [(i * i / 100000) for i in array_size_range]

    plt.subplot(122)
    plt.plot(array_size_range, n_logn)
    plt.axis([500, 700, 0.03, 0.12])
    plt.title('N log N Normalized vs Array Size')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    qs_time()
