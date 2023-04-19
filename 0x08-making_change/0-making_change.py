#!/usr/bin/python3

"""

    Module: 0-make_change

"""


def makeChange(coins, total):
    """
        Function that makes change of the total from the coins
        Params: coins
                total
        Return: fewest number of coins needed to meet total
                If total is 0 or less, return 0
                If total cannot be met by any number of coins you have,
                return -1
    """
    # least coins
    coin_count = 0
    if total > 0:
        while total > 0 and coins:
            greatest = max(coins)
            if greatest < total:
                while greatest < total:
                    total -= greatest
                    coin_count += 1

                coins.remove(greatest)
            elif any(total<x for x in coins):
                return -1

        return coin_count

    return 0
