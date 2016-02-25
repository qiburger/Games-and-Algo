"""
Coins are of values 1 = v_1 < v_2 < ... < v_n
v_1 can make change to anything
Algorithm which makes change for an amount of money $A$ with as few coins as possible

"""


def make_change(amount, coin_list, memoization):
    memoization[0] = 0
    memoization[1] = 1
    for a in range(2, amount + 1):
        memoization[a] = a  # default to all value to max change with 1 coins
        for coin in coin_list:
            if coin <= a:
                memoization[a] = min(memoization[a - coin] + 1, memoization[a])
    return memoization[amount]
