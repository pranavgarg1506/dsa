## https://leetcode.com/problems/2-keys-keyboard/


"""
There is only one character 'A' on the screen of a notepad. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.
"""

n = 4

## method 1 Mathematical Solution
dp = [0] * (n+1)

dp[0] = dp[1] = 0
for i in range(2, n+1):
    dp[i] = i
    for j in range(i-1, 1, -1):
        if i % j == 0:
            dp[i] = dp[j] + int(i/j)
            break

print(dp[-1])


## Method 2 DP solution

