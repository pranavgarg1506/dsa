## Triangle

"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
"""


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
"""
2                                2
3 4                              5  6
6 5 7      ==>                   11 10 13
4 1 8 3                          15 11 18 16

"""

## since first row contains only 1 element, it would be considered in the final answer
## so starting from the row index 1

for i in range(1, len(triangle)):
    
    ## traversing in the row
    for j in range(  len(triangle[i])  ):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == len(triangle[i]) - 1:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += min( triangle[i-1][j-1], triangle[i-1][j] )

print(triangle)
print(min(triangle[-1]))



