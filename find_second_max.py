'''
    Algorithm that compute the second smallest element
    in an array of integers.
'''
import random


def find_sec_max(list_in):
    """
    :type list_in: list (array in python)
    """

    if len(list_in) < 2: return None

    largest = max(list_in[0], list_in[1])
    second = min(list_in[0], list_in[1])

    for i in range(len(list_in)):
        if i > 1:
            if list_in[i] > second:
                second = list_in[i]
                if second > largest:
                    temp = second
                    second = largest
                    largest = temp
    return second


def tester(list_in):
    if len(list_in) < 2: return None
    new_list = list(list_in)
    new_list.remove(max(new_list))
    return max(new_list)


if __name__ == "__main__":

    for i in range(-100, 100):
        for j in range(0, 20):
            test = random.sample(range(100), j)
            if find_sec_max(test) != tester(test):
                print test
                print find_sec_max(test)
                print tester(test)
                print '-----'
                break
