#!/usr/bin/env python

__author__ = 'natasha'

def CoinDeterminer(num):
    coins = [1, 5, 7, 9, 11]

    if num in coins:
        return 1

    # list of calculated minimum number of coins for specific change values x
    min_amounts= [-1] * (num+1)  # F(x)
    # denomination value of zero produces 0 amount of coins
    min_amounts[0] = 0

    # F(x) = 1 + min(F(x-i)) for all i in coins if i <= x
    for x in range(1, num+1):
        minimum = -1
        for i in coins:
            index = x - i
            if index >= 0:
                if (min_amounts[index] < minimum) or (minimum == -1):
                    minimum = min_amounts[index]
            else:
                break
        min_amounts[x] = 1 + minimum

    return min_amounts[num]


