## https://www.geeksforgeeks.org/find-the-minimum-cost-to-reach-a-destination-where-every-station-is-connected-in-one-direction/

MAX_VALUE = 321456987

cost = [ [0, 15, 80, 90],
         [float("inf"), 0, 40, 50],
         [float("inf"), float("inf"), 0, 70],
         [float("inf"), float("inf"), float("inf"), 0]
        ]
n = len(cost)


"""
0     15    80    90
inf   0     40    50
inf   inf   0     70
inf   inf   inf   0
"""

dp = [MAX_VALUE] * (n)

dp[0] = 0

"""

stat 1
dp[1] = cost[0][1]


stat 2
dp[2] = min( dp[0] + cost[0][2], dp[1] + cost[1][2]  )
"""

for i in range(1,n):
    for j in range(0, i):
        dp[i] = min(dp[i] , dp[j] + cost[j][i])
print(dp)
print(dp[-1])