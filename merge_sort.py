

def merge_sort(array):
    """
    :type array: list
    """
    if len(array) == 1: return array

    mid = len(array) / 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    merged = []

    #edge case 1
    if left[-1] < right[0]:
        merged = left + right

    #edge case 2
    elif right[-1] < left[0]:
        merged = right + left

    else:
        #merge with two pointers
        ptr_left = 0
        ptr_right = 0

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
