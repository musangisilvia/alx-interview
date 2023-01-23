"""
    a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n

        Returns an empty list if n <= 0
        assumes n will be always an integer

"""
from math import factorial

def pascal_triangle(n):
    list_lists = []
    small_list = []
    if n <= 0:
        return list_lists
    else:
        for i in range(n):
            for j in range(i+1):
                # nCr = n!/((n-r)!*r!)
                small_list.append(factorial(i)//(factorial(j)*factorial(i-j)))

            list_lists.append(small_list)
            small_list = []

        return list_lists