## link = https://leetcode.com/problems/minimum-path-sum/


"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

grid = [[1,3,1],[1,5,1],[4,2,1]]
"""
1 3 1       1 4 5
1 5 1  ==>  2  
4 2 1       6
"""

for i in range(1, len(grid[0])):
    grid[i][0] += grid[i-1][0]

for i in range(1, len(grid[1])):
    grid[0][i] += grid[0][i-1]

#print(grid)

for row in range(1, len(grid[0])):
    for col in range(1, len(grid[1])):
        grid[row][col] += min( grid[row-1][col], grid[row][col-1] )

print(grid[-1][-1])