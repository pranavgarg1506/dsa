## https://leetcode.com/problems/coin-change/

"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

coins = [1,2,5]
amount = 11

dp = [amount + 1] * (amount+1)
dp[0] = 0

for i in range(1, amount+1):

    for c in coins:
        if c <= i:
            dp[i] = min(dp[i], dp[i-c] + 1)
if dp[amount] == amount+1:
    print(-1)
else:
    print(dp[-1])