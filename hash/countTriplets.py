#!/usr/local/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

geometricProgressionMax = 3

# Although this solution is nice, it doesn't take into account the constraint of ascending order, the counter breaks it
# def countTriplets(arr, r):
# 	count = 0
# 	amountOfValues = Counter(arr)
# 	print(amountOfValues)

# 	for key in amountOfValues.keys():
# 		if key == 0 and amountOfValues[key] > 2:
# 			count += int(amountOfValues[key]*(amountOfValues[key]-1)/2)
# 		elif r == 1 and amountOfValues[key] > 2:
# 			count += int(amountOfValues[key]*(amountOfValues[key]-1)/2)
# 		else: 
# 			localProgressionTriplets = 1
# 			for geometricProgression in range(geometricProgressionMax):
# 				localProgressionTriplets *= amountOfValues[key*(r**geometricProgression)]

# 			count += localProgressionTriplets

# 	return count		

# Complete the countTriplets function below.
def countTriplets(arr, r):
	
	

if __name__ == '__main__':
	nr = input().rstrip().split()

	n = int(nr[0])

	r = int(nr[1])

	arr = list(map(int, input().rstrip().split()))

	ans = countTriplets(arr, r)
	print(ans)
