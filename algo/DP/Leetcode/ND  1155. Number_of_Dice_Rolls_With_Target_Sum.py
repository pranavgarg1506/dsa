## https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

"""
You have d dice and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 109 + 7 to roll the dice so the sum of the face-up numbers equals target.
"""

d = 2
f = 7
target = 8

dp = [ 0 for i in range(d*f+1)]
dp[]


for i in range(d, target+1):
    dp[i] = 