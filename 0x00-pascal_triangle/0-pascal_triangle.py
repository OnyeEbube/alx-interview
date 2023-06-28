#!/usr/bin/python3
"""
A module that contains the pascal_triangle(n) function
"""

def pascal_triangle(n):
    """
    This function returns a list of lists of integers representing
    the Pascal's triangle of n
    """
    my_list = []
    if n <= 0:
        return my_list
    for i in range(n):
        row = [1]
        if my_list:
            prev_row = my_list[-1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        my_list.append(row)
    return my_list

