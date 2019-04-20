#!/usr/local/bin/python3

import math
import os
import random
import re
import sys


def selectionSort(alist):
	swaps = 0
	for index in range(0, len(alist)):
		minimum_key = index
		minimum_value = alist[index]
		for index2 in range(index, len(alist)):
			if alist[index2] < minimum_value:
				minimum_key = index2
				minimum_value = alist[index2]
		if minimum_value != alist[index]:
			alist[index], alist[minimum_key] = alist[minimum_key], alist[index]
			swaps +=1

	return swaps


# Complete the minimumSwaps function below.
def minimumSwaps(alist):
	return selectionSort(alist)

if __name__ == '__main__':
	n = int(input())

	q = list(map(int, input().rstrip().split()))

	print(minimumSwaps(q))