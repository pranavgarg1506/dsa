## https://leetcode.com/problems/unique-paths/

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""
m = 3
n = 7

## for travelling in the edges only 1 way is possible

dp = [ [1 for j in range(n)] for i in range(m)]
print(dp)


for i in range(1,m):
    for j in range(1,n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[-1][-1])