#!/usr/local/bin/python3

import math
import os
import random
import re
import sys

def merge(itemsA, itemsB):
	merged = [0]*(len(itemsA)+len(itemsB))

	indexA, indexB = 0, 0

	amountofInversions = 0

	while indexA+indexB < len(merged):		
		if itemsA[indexA] <= itemsB[indexB]:
			merged[indexA+indexB] = itemsA[indexA]
			indexA += 1
		else:
			merged[indexA+indexB] = itemsB[indexB]
			indexB += 1
			amountofInversions += len(itemsA)-indexA

		if indexA == len(itemsA):
			merged[indexA+indexB:] = itemsB[indexB:]
			indexB = len(itemsB)
		if indexB == len(itemsB):
			merged[indexA+indexB:] = itemsA[indexA:]
			amountofInversions += len(itemsA)*(len(itemsB)-indexB)
			indexA = len(itemsA)

	return merged, amountofInversions

def mergeSort(items):
	if len(items) <= 1:
		return items, 0

	half = int(len(items)/2)
	mergedLeft, inversionsLeft = mergeSort(items[0:half])
	mergedRight, inversionsRight = mergeSort(items[half:])
	merged, amountOfInversions = merge(mergedLeft, mergedRight)

	return merged, amountOfInversions+inversionsLeft+inversionsRight


# Complete the countInversions function below.
def countInversions(arr):
	merged, inversions = mergeSort(arr)
	return inversions

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)
        print(result)
