#!/usr/bin/python3
"""
    a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n

        Returns an empty list if n <= 0
        assumes n will be always an integer

"""


def pascal_triangle(n):
    """
        Function to return list of lists
        parameter: n (nth number)
        return: empty list if n <= 0 or list of lists
    """
    list_lists = []
    small_list = []
    if n <= 0:
        return list_lists
    else:
        for i in range(n):
            for j in range(i+1):
                # nCr = n!/((n-r)!*r!)
                small_list.append(factorial_(i)//(factorial_(j) *
                                  factorial_(i-j)))

            list_lists.append(small_list)
            small_list = []

        return list_lists


def factorial_(n):
    """
        Function to find factorial
        parameter: n
        return: factorial of a number
    """
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i

    return factorial
