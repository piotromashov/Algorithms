#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.

def sortBySock(n, ar):
    socksSorted = [0]*100
    for i in range(n):
        socksSorted[ar[i]-1] += 1
    return socksSorted

def sockMerchant(n, ar):
    pairs = 0
    socksSorted = sortBySock(n, ar)

    for socksAmount in socksSorted:
        pairs += math.floor(socksAmount/2)
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
