# #200. Number of Islands
# Medium

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of
# islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
# all four edges of the grid are all surrounded by water.
#
#
#
# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
#


def num_islands(grid):
    a_list = []
    # for i in grid:
    #     for j in i:
    if grid is None:
        return 0

    m = len(grid)
    if m == 0:
        return 0

    n = len(grid[0])
    if n == 0:
        return 0

    a = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j]=='1':
                a+=1
                dfs(grid, i, j, m, n)
    return a


def dfs(g, i , j, m, n):
    if i < 0 or j<0 or i>=m or j>=n or g[i][j]=='0':
        return

    g[i][j] = '0'

    dfs(g, i-1, j, m, n)
    dfs(g, i+1, j, m, n)
    dfs(g, i, j-1, m, n)
    dfs(g, i, j+1, m, n)


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(num_islands(grid))