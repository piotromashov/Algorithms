#!/bin/python3
#https://www.hackerrank.com/challenges/ctci-coin-change
import sys

def make_change(coins, n):
    dp = [1] + [0] * n
    
    for coin in coins:
        for i in range(coin, n+1):
            dp[i] += dp[i-coin]
    return dp[n]
    

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
coins.sort()
print(make_change(coins, n))