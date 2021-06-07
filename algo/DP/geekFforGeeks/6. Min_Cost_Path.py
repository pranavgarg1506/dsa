## https://www.geeksforgeeks.org/min-cost-path-dp-6/
"""
User can move right or downwards or diagonally right
"""

cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]

for i in range(1,len(cost)):
    cost[0][i] += cost[0][i-1]

for i in range(1,len(cost)):
    cost[i][0] += cost[i-1][0]

for row in range(1, len(cost)):
    for col in range(1, len(cost)):
        cost[row][col] += min(cost[row][col-1], cost[row-1][col], cost[row-1][col-1])

        
print(cost)
print(cost[-1][-1])
