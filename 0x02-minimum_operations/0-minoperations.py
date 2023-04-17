#!/usr/bin/python3

"""
    Module: 0-minoperations
"""


def minOperations(n):
    """
            Function: minOperations
            returns the number of operations performed to reach n
            characters
            params: n
            return: 0 if n is impossible
    """

    # Logic: using prime factors find the minimum number
    # of operations

    # function to find smallest prime factor for n
    def smallestPrimeFactor(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return i
        return n

    minimumoperations = 0
    while n > 1:
        smallest_prime = smallestPrimeFactor(n)

        if smallest_prime == n:
            return minimumoperations + smallest_prime

        # count number of times smallest prime is in n
        count = 0
        while n % smallest_prime == 0:
            n //= smallest_prime
            count += 1

        minimumoperations += smallest_prime * count

    return minimumoperations
