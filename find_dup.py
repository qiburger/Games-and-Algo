'''
Find duplicates in an array of int
'''

import merge_sort


def find_dup_via_sort(array):
    """
    :type array: list of int
    :return the smallest duplicates
    """
    sorted_array = merge_sort.merge_sort(array)
    for i in range(len(sorted_array)):
        if i > 0:
            if sorted_array[i - 1] == sorted_array[i]: return sorted_array[i]
    return None


def find_dup(array):
    """
    :type array: list of positive integers
    :return list of all duplicates
    """
    checking_array = []
    dups = []

    # check if list is empty
    if len(array)<1:
        return None

    # first find the largest element
    max_element = array[0]
    for element in array:
        max_element = max(max_element, element)

    # next make an array of 0s with size as largest as the largest element in given array
    for i in range(max_element + 1):
        checking_array.append(0)

    # then map each element to the new array with index = value of the element
    for j in array:
        if j < 0: raise ValueError
        checking_array[j] += 1

    # now check if there are duplicates
    for k in range(len(checking_array)):
        if checking_array[k] > 1:
            dups.append(k)

    return dups
