## https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/



coins = [9,6,5,1]
amount = 11
dp = [amount+1] * (amount+1)
sorted(coins)
print(coins)

dp[0] = 0

for i in range(1,amount+1):

    dp[i]=i
    for c in coins:
        if c <= i:
            dp[i] = min(dp[i], dp[i-c]+1)

#print(dp)

if dp[amount] == amount + 1:
    print(-1)
else:
    print(dp[amount])