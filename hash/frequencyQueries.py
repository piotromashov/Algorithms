#!/usr/local/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, defaultdict

def incrementAppearances(value, counter, frequency):
	if frequency.get(counter[value]):
		frequency[counter[value]].remove(value)		# remove that value amount of appeareances
	counter[value] += 1										# add the value to the counter
	frequency[counter[value]].append(value)			# add that value amount of appeareances	

def decrementAppearances(value, counter, frequency):
	if frequency.get(counter[value]):
		frequency[counter[value]].remove(value)		# remove that value amount of appeareances
	counter[value] = max(counter[value]-1, 0)				# decrement the value to the counter
	if counter[value] > 0:
		frequency[counter[value]].append(value)			# add that value amount of appeareances

Complete the freqQuery function below.
def freqQuery(queries):
	counter = Counter()		# store the value -> amount of appearances
	frequency = defaultdict(list)	# store the amount of appearances -> list of values

	results = []
	for q, value in queries:
		if q == 1:
			incrementAppearances(value, counter, frequency)
		if q == 2:
			decrementAppearances(value, counter, frequency)
		if q == 3:
			results.append(1 if frequency.get(value, 0) else 0)

	return results


# Another way to do it!
# def freqQuery(queries):
# 	freq = Counter()
# 	cnt = Counter()
# 	arr = []

# 	for q in queries:
# 		if q[0]==1:
# 			cnt[freq[q[1]]]-=1
# 			freq[q[1]]+=1
# 			cnt[freq[q[1]]]+=1

# 		elif q[0]==2:
# 			if freq[q[1]]>0:
# 				cnt[freq[q[1]]]-=1
# 				freq[q[1]]-=1
# 				cnt[freq[q[1]]]+=1

# 		else:
# 			if cnt[q[1]]>0:
# 				arr.append(1)
# 			else:
# 				arr.append(0)

# 	return arr
	

if __name__ == '__main__':
	q = int(input().strip())

	queries = []

	for _ in range(q):
		queries.append(list(map(int, input().rstrip().split())))

	ans = freqQuery(queries)
	print(ans)