#!/usr/bin/python3
"""
A module that holds a lockbox function
"""


def canUnlockAll(boxes):
    """
    A function that unlocks boxes
    """
    unlocked = set([0])
    stack = [0]

    while stack:
        box = stack.pop()
        keys = boxes[box]

        for key in keys:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == len(boxes)
