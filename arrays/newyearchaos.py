#!/usr/local/bin/python3

import math
import os
import random
import re
import sys

maximum_amount_of_bribes = 2

# this doesn't work because of this scenario, 8 and 4
# 1 2 5 3 7 8 6 4
# 1 2 3 4 5 6 7 8
def isValid(q):
	for key, value in enumerate(q):
		if abs(key+1 - value) > 2:
			return False
	return True

def reversedInsertionSort(alist):
	total_bribes = 0
	max_local_bribes = 0
	for i in range(len(alist)-2, -1, -1):
		current = alist[i]

		bribes = 0
		while i < len(alist)-1 and current>alist[i+1]:
			# print("{}, {}".format(alist[i], alist[i+1]))
			alist[i] = alist[i+1]
			i += 1
			alist[i] = current
			bribes += 1

		if bribes > max_local_bribes:
			max_local_bribes = bribes

		total_bribes+=bribes


	return max_local_bribes, total_bribes

def minimumBribes(q):
	max_local_bribes, total_bribes = reversedInsertionSort(q)
	if max_local_bribes > maximum_amount_of_bribes:
		print("Too chaotic")
	else:
		print(total_bribes)


	#q[i], q[j] = q[j], q[i]

if __name__ == '__main__':
	t = int(input())

	for t_itr in range(t):
		n = int(input())

		q = list(map(int, input().rstrip().split()))

		minimumBribes(q)


