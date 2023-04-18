# #2617. Minimum Number of Visited Cells in a Grid
# Hard
# 203
# 18
# Companies
# You are given a 0-indexed m x n integer matrix grid. Your initial position is at the top-left cell (0, 0).
#
# Starting from the cell (i, j), you can move to one of the following cells:
#
# Cells (i, k) with j < k <= grid[i][j] + j (rightward movement), or
# Cells (k, j) with i < k <= grid[i][j] + i (downward movement).
# Return the minimum number of cells you need to visit to reach the bottom-right cell (m - 1, n - 1). If there is no
# valid path, return -1.
#
#
#
# Example 1:
#
#
# Input: grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
# Output: 4
# Explanation: The image above shows one of the paths that visits exactly 4 cells.
# Example 2:
#
#
# Input: grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
# Output: 3
# Explanation: The image above shows one of the paths that visits exactly 3 cells.
# Example 3:
#
#
# Input: grid = [[2,1,0],[1,0,0]]
# Output: -1
# Explanation: It can be proven that no path exists.
from collections import deque

from sortedcontainers import SortedList

def mini_visited_cells(grid):
    m = len(grid)
    n = len(grid[0])
    s0 = [SortedList(range(n)) for _ in range(m)]
    s1 = [SortedList(range(m)) for _ in range(n)]
    q = deque([(0,0,1)])
    while q:
        i, j, d = q.popleft()
        if (i, j) == (m-1, n-1):
            return d
        for k in list(s0[i].irange(j+1, min(j+1+grid[i][j], n) - 1)):
            q.append((i, k, d+1))
            s0[i].remove(k)
            s1[k].remove(i)
        for k in list(s1[j].irange(i+1, min(i+1+grid[i][j], m)-1)):
            q.append((k, j, d+1))
            s1[j].remove(k)
            s0[k].remove(j)
    return -1


if __name__ == '__main__':
    print(mini_visited_cells([[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]))
    print(mini_visited_cells([[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]))
    print(mini_visited_cells([[2,1,0],[1,0,0]]))