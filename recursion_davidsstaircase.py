#https://www.hackerrank.com/challenges/ctci-recursive-staircase
def ways_to_jump(n):
    memo = [0,1,2,4]
    for i in range(4, n+1):
        memo.append(memo[i-1]+memo[i-2]+memo[i-3])
    return memo[n]

s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(ways_to_jump(n))