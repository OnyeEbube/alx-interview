#!/usr/bin/python3
"""
A function
"""


def isWinner(x, nums):
    def isPrime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def canWin(n):
        primes = [i for i in range(2, n + 1) if isPrime(i)]
        dp = [False] * (n + 1)
        dp[0] = False  # Maria loses when there are no numbers left
        dp[1] = False  # Maria loses when only 1 is left
        dp[2] = True   # Maria wins when 2 is left
        dp[3] = True   # Maria wins when 3 is left

        for i in range(4, n + 1):
            for prime in primes:
                if prime > i:
                    break
                if not dp[i - prime]:
                    dp[i] = True
                    break

        return dp[n]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if canWin(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
