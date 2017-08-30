#https://www.hackerrank.com/challenges/ctci-big-o
from math import *

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, floor(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# def isPrime(n):
#     if n <= 1:
#         return False
#     return sieveOfEratosthenes(n)[n]

# def sieveOfEratosthenes(n):
#     sieve = [1]*(n+1)
#     for key in range(2, n+1):
#         markMultiplesNotPrime(sieve, key)
#     return sieve
        
# def markMultiplesNotPrime(sieve, key):
#     index = key*key
#     while index < len(sieve):
#         sieve[index] = 0
#         index += key    

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    if isPrime(n):
        print("Prime")
    else:
        print("Not prime")