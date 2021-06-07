## https://www.geeksforgeeks.org/cutting-a-rod-dp-13/



arr = [4, 5, 8, 9, 10, 16, 17, 20]

n = len(arr)

dp = [0] * (n+1)


for i in range(1, n+1):

    for j in range(0, i):
        dp[i] = max(dp[i], arr[j] + dp[i-j-1] )


print(dp)
