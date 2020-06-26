#!/usr/local/bin/python3

import math
import os
import random
import re
import sys

def getSwaps(arr, sortedArr):
	swaps = 0
	value_to_index = {}
	for i in range(len(arr)):
		value_to_index[arr[i]] = i

	for index in range(len(arr)):
		if arr[index] != sortedArr[index]:
			swaps += 1

			index_to_swap = value_to_index[sortedArr[index]]
			value_to_index[arr[index]] = value_to_index[sortedArr[index]]
			arr[index], arr[index_to_swap] = sortedArr[index], arr[index]
	return swaps

# Complete the lilysHomework function below.
def lilysHomework(arr):
	sortedArr = sorted(arr)
	unorderedElements = getSwaps(list(arr), sortedArr)
	unorderedElementsReversed = getSwaps(list(reversed(arr)), sortedArr)

	return min(unorderedElements, unorderedElementsReversed)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)
    print(result)
