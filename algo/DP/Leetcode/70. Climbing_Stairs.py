## https://leetcode.com/problems/climbing-stairs/


"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


"""
n = 1
1

n = 2
1,1    2

n = 3
1,1,1    1,2   2,1
"""

n = 9

dp = [0] * (n+1)

dp[0] = 1
dp[1] = 1

## for iterating over the number of steps
for i in range(2,n+1):
    ## for traversing the number of sizes
    for way in range(1,3):
        dp[i] += dp[i-way]

print(dp[1:])
print(dp[-1])

