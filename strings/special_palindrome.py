#!/bin/python3

import math
import os
import random
import re
import sys


def isSpecial(s):
    if len(s) == 0:
        return False
    first_char = s[0]
    for k, v in enumerate(s):
        if k == len(s) // 2 and len(s) % 2 == 1:
            continue
        if v != first_char:
            return False
    return True


# Complete the substrCount function below.
def substrCount(n, s):
    special_substrings = 0
    for i in range(n):
        for j in range(i, n):
            if isSpecial(s[i:j+1]):
                special_substrings += 1
    return special_substrings


if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
