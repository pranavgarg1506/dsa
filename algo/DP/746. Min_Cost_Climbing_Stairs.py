
# https://leetcode.com/problems/min-cost-climbing-stairs/

"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""

cost = [10,15,20]

if len(cost) == 2:
    print(cost[1] if cost[0] > cost[1] else cost[0])
else:
    for i in range(2, len(cost)):
        cost[i] += min(cost[i-1], cost[i-2])

    print(cost[-1] if cost[-2] > cost[-1] else cost[-2])

