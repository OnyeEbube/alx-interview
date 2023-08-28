#!/usr/bin/python3
"""
A function
"""


def makeChange(coins, total):
    """
    Returns fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    min_coins = [float('inf')] * (total + 1)

    min_coins[0] = 0
    for coin in coins:
        for amount in range(coin, total + 1):
            min_coins[amount] = min(
                    min_coins[amount], min_coins[amount - coin] + 1)
    return min_coins[total] if min_coins[total] != float('inf') else -1
