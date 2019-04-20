#!/usr/local/bin/python3

import math
import os
import random
import re
import sys

def hourglass(aXindex, aYindex, aMatrix):
	top_line = aMatrix[aYindex][aXindex]+aMatrix[aYindex][aXindex+1]+aMatrix[aYindex][aXindex+2]
	center = aMatrix[aYindex+1][aXindex+1]
	bottom_line = aMatrix[aYindex+2][aXindex]+aMatrix[aYindex+2][aXindex+1]+aMatrix[aYindex+2][aXindex+2]

	return top_line+center+bottom_line

# Complete the arrayManipulation function below.
def hourglassSum(aMatrix):
	# check if valid matrix
	max_hourglass = float("-infinity")
	for x in range(0, len(aMatrix)-2):
		for y in range(0, len(aMatrix)-2):
			hourglass_sum = hourglass(x, y, aMatrix)

			if hourglass_sum > max_hourglass:
				max_hourglass = hourglass_sum

	return max_hourglass

if __name__ == '__main__':
	arr = []

	for _ in range(6):
		arr.append(list(map(int, input().rstrip().split())))

	result = hourglassSum(arr)

	print(result)