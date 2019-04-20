#!/usr/local/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
	alist = [0]*(n+1)

	for left_index, right_index, increment in queries:
		alist[left_index-1] += increment
		if right_index <= n:
			alist[right_index] -= increment

	maximum = 0
	added_value = 0
	for x in alist:
		added_value += x
		if added_value > maximum:
			maximum = added_value
			
	return maximum


if __name__ == '__main__':
	n, m = map(int, input().split())

	queries = []

	for _ in range(m):
		queries.append(list(map(int, input().rstrip().split())))

	result = arrayManipulation(n, queries)
	print(result)