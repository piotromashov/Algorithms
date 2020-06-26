#!/usr/local/bin/python3

import math
import os
import random
import re
import sys


def stringsIntersect(s1, s2):
	for char in "abcdefghijklmnopqrstuvwxyz":
		if char in s1 and char in s2:
			return True
	return False

def twoStrings(s1, s2):
	return "YES" if stringsIntersect(s1, s2) else "NO"

if __name__ == '__main__':
	q = int(input())

	for q_itr in range(q):
		s1 = input()

		s2 = input()

		result = twoStrings(s1, s2)
		print(result)
