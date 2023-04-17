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
    # min operations done = 2
    copy_a = 1
    paste = 1

    min_ops = n

    all_ops = 0

    man_operations = copy_a + paste

    for i in (man_operations, n):
        all_ops = n - copy_a - paste
        if (all_ops + (all_ops * paste)) > min_ops:
            min_ops = all_ops + (all_ops * paste)
        
        paste = paste + 1

    return min_ops