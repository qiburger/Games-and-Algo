import numpy as np


def merge_four(array):
    """
    :type array: list
    """
    if len(array) <= 1:
        return array

    if len(array) == 2:
        return [min(array[0], array[1]), max(array[0], array[1])]

    mid = len(array) / 2
    first = mid / 2
    third = (len(array) - mid) / 2 + mid

    one = merge_four(array[:first])
    two = merge_four(array[first:mid])
    three = merge_four(array[mid:third])
    four = merge_four(array[third:])

    merged = []

    #merge with four pointers
    ptr_one = 0
    ptr_two = 0
    ptr_three = 0
    ptr_four = 0

    #merge four
    while ptr_one < len(one) and ptr_two < len(two) and ptr_three < len(three) and ptr_four < len(four):
        if one[ptr_one] <= min (two[ptr_two], three[ptr_three], four[ptr_four]) :
            merged.append(one[ptr_one])
            ptr_one += 1
        elif two[ptr_two] <= min (one[ptr_one], three[ptr_three], four[ptr_four]) :
            merged.append(two[ptr_two])
            ptr_two += 1
        elif three[ptr_three] <= min (one[ptr_one], three[ptr_three], four[ptr_four]) :
            merged.append(three[ptr_three])
            ptr_three += 1
        else:
            merged.append(four[ptr_four])
            ptr_four += 1

    if ptr_one >= len(one):
        merged.extend(merge_three(two, ptr_two, three, ptr_three, four, ptr_four))
    elif ptr_two >= len(two):
        merged.extend(merge_three(one, ptr_one, three, ptr_three, four, ptr_four))
    elif ptr_three >= len(three):
        merged.extend(merge_three(two, ptr_two, one, ptr_one, four, ptr_four))
    else:
        merged.extend(merge_three(two, ptr_two, one, ptr_one, three, ptr_three))

    return merged


def merge_three(one, ptr_one, two, ptr_two, three, ptr_three):
    merged = []
    while ptr_one < len(one) and ptr_two < len(two) and ptr_three < len(three):
        if one[ptr_one] <= min (two[ptr_two], three[ptr_three]) :
            merged.append(one[ptr_one])
            ptr_one += 1
        elif two[ptr_two] <= min (one[ptr_one], three[ptr_three]) :
            merged.append(two[ptr_two])
            ptr_two += 1
        else:
            merged.append(three[ptr_three])
            ptr_three += 1


    if ptr_one >= len(one):
        merged.extend(merge_two(two, ptr_two, three, ptr_three))
    elif ptr_two >= len(two):
        merged.extend(merge_two(one, ptr_one, three, ptr_three))
    else:
        merged.extend(merge_two(two, ptr_two, one, ptr_one))

    return merged


def merge_two(left, ptr_left, right, ptr_right):
    merged = []

    while ptr_left < len(left) and ptr_right < len(right):
        if left[ptr_left] <= right[ptr_right]:
            merged.append(left[ptr_left])
            ptr_left += 1
        else:
            merged.append(right[ptr_right])
            ptr_right += 1

    merged.extend(left[ptr_left:])
    merged.extend(right[ptr_right:])

    return merged

def test1(n):
    for i in range(100):
        array = list(np.random.choice(100, n, replace=None))
        merged = merge_four(array)
        if merged != sorted(array):
            print array
            print merged
            break

