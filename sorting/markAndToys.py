#!/usr/local/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
	prices = sorted(prices)
	left_to_spend = k
	toys = 0
	for price in prices:
		if left_to_spend - price > 0:
			left_to_spend -= price
			toys += 1
		else:
			break
	return toys

if __name__ == '__main__':
	nk = input().split()

	n = int(nk[0])

	k = int(nk[1])

	prices = list(map(int, input().rstrip().split()))

	result = maximumToys(prices, k)
	print(result)