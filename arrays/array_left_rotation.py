#!/usr/local/bin/python3

def array_left_rotation(a, k):
    return a[k:]+a[0:k]
    

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, k);
print(*answer, sep=' ')
