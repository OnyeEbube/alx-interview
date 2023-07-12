#!/usr/bin/env python3
"""
A method that calculates the fewest number of operations needed to result in
exactly n H characters in the file"""


def minOperations(n):
    """This function calculates the minimum Operation"""
    if n == 1:
        return 0

    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return minOperations(i) + (n // i)
    return n
