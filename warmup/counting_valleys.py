#!/usr/local/bin/python3
# https://www.hackerrank.com/challenges/counting-valleys

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
	currentLevel = 0
	timesBelowZero = 0
	prevLevel = 1

	for i in range(n):
		if s[i] == "U":
			currentLevel += 1
		else:
			currentLevel -= 1

		if prevLevel == 1 and currentLevel < 0:
			prevLevel = -1
			timesBelowZero += 1
		elif prevLevel == -1 and currentLevel >= 0:
			prevLevel = 1

	return timesBelowZero

if __name__ == '__main__':
	fptr = sys.stdout

	n = int(input())

	s = input()

	result = countingValleys(n, s)

	fptr.write(str(result) + '\n')
	fptr.close()