#!/usr/local/bin/python3
#https://www.hackerrank.com/challenges/repeated-string/problem

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    occurrences = 0
    occurrences_coefficient = s.count('a')
    occurrences = occurrences_coefficient * math.floor(n/len(s)) + s[0:n % len(s)].count('a')
    return occurrences
    # index = 0
    # occurences = 0
    # while index < n:
    #     if s[index % len(s)] == 'a':
    #         occurrences += 1
    #     index += 1
    # return occurrences

if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
