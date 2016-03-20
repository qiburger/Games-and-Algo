__author__ = 'QHe'

L = [1, 2, 3, [3, 4]]

def cumulative_sum(L):
    cumulator = []
    total = 0
    for x in L:
        if isinstance(x, list):
            cumulator.append(cumulative_sum(x))
        else:
            total = total + x
            cumulator.append(total)
    return cumulator

print cumulative_sum(L)

