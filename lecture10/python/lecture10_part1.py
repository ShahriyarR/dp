def max_profit_reconstruct_path(grid: list[list[int]]) -> list[list[int]]:
    """
    Problem:
	Maximum Profit in a Grid (homework for lecture9)

	A robot is located at the top-left corner of a m x n grid (marked 'S' in the diagram below).
	The robot can only move either down or right at any point in time.
	The robot is trying to reach the bottom-right corner of the grid (marked 'E' in the diagram below).
	Each cell contains a coin the robot can collect.

	What is the path that lead to the maximum profit the robot can accumulate?

	+---+---+---+---+
	| S | 2 | 2 | 1 |
	+---+---+---+---+
	| 3 | 1 | 1 | 1 |
	+---+---+---+---+
	| 4 | 4 | 2 | E |
	+---+---+---+---+

    Time complexity: O(mn)
    Space complexity: O(mn)
    """

    m = len(grid)
    n = len(grid)

    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            dp[i][j] = grid[i][j]

            if i > 0 and j > 0:
                dp[i][j] += max(dp[i-1][j], dp[i][j-1])
            elif i > 0:
                dp[i][j] += dp[i-1][j]
            elif j > 0:
                dp[i][j] += dp[i][j-1]
        path = []
        return get_path(dp, m-1, n-1, path)
    


def get_path(dp: list[list[int]], i: int, j: int, path: list[list[int]]) -> list[list[int]]:
   if i == 0 and j == 0:
       return path + [[i, j]]
   elif i == 0:
       path = get_path(dp, i, j-1, path)
   elif j == 0:
       path = get_path(dp, i-1, j, path)
   else:
       if dp[i-1][j] > dp[i][j-1]:
           path = get_path(dp, i-1, j, path)
       else:
           path = get_path(dp, i, j-1, path)
   return path + [[i, j]]