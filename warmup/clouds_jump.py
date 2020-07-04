#!/usr/local/bin/python3
#https://www.hackerrank.com/challenges/jumping-on-the-clouds/

import math
import os
import random
import re
import sys

def attemptJump(c, current_cloud):
	if current_cloud + 2 < len(c) and c[current_cloud + 2] == 0:
		return 2
	if current_cloud + 1 < len(c) and c[current_cloud + 1] == 0:
		return 1
	return 0

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
	jumps = 0
	current_cloud = 0

	while current_cloud < len(c)-1:
		current_cloud += attemptJump(c, current_cloud)
		jumps += 1
	return jumps
		
if __name__ == '__main__':
	fptr = sys.stdout

	n = int(input())

	c = list(map(int, input().rstrip().split()))

	result = jumpingOnClouds(c)

	fptr.write(str(result) + '\n')

	fptr.close()
