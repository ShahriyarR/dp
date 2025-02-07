def max_profit(grid: list[list[int]]) -> int:
    """
    Problem:
	Maximum Profit in a Grid

	A robot is located at the top-left corner of a m x n grid (marked 'S' in the diagram below).
	The robot can only move either down or right at any point in time.
	The robot is trying to reach the bottom-right corner of the grid (marked 'E' in the diagram below).
	Each cell contains a coin the robot can collect.

	What is the maximum profit the robot can accumulate?

	+---+---+---+---+
	| S | 2 | 2 | 1 |
	+---+---+---+---+
	| 3 | 1 | 1 | 1 |
	+---+---+---+---+
	| 4 | 4 | 2 | E |
	+---+---+---+---+

    Time complexity:
    Space complexity:
    f(i,j) = max(f(i-1, j), f(i, j-1)) + grid(i,j)

    """

    m = len(grid)
    n = len(grid[0])

    dp = [[0] * n for _ in range(m)]

    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            dp[i][j] = grid[i][j]

            if i > 0 and j > 0:
                dp[i][j] += max(dp[i-1][j], dp[i][j-1])
            elif i > 0:
                dp[i][j] += dp[i-1][j]
            elif j > 0:
                dp[i][j] += dp[i][j-1]
    # Input Grid:
    # [ 0  2  2  50]
    # [ 3  1  1 100]
    # [ 4  4  2   0]

    # DP States:

    # Initial state (dp[0][0] = grid[0][0]):
    # [ 0  0  0   0]
    # [ 0  0  0   0]
    # [ 0  0  0   0]

    # After (0,1): value + left
    # [ 0  2  0   0]
    # [ 0  0  0   0]
    # [ 0  0  0   0]

    # After (0,2): value + left
    # [ 0  2  4   0]
    # [ 0  0  0   0]
    # [ 0  0  0   0]

    # After (0,3): value + left
    # [ 0  2  4  54]
    # [ 0  0  0   0]
    # [ 0  0  0   0]

    # After (1,0): value + up
    # [ 0  2  4  54]
    # [ 3  0  0   0]
    # [ 0  0  0   0]

    # After (1,1): value + max(up,left)
    # [ 0  2  4  54]
    # [ 3  4  0   0]
    # [ 0  0  0   0]

    # After (1,2): value + max(up,left)
    # [ 0  2  4  54]
    # [ 3  4  5   0]
    # [ 0  0  0   0]

    # After (1,3): value + max(up,left)
    # [ 0  2  4  54]
    # [ 3  4  5 154]
    # [ 0  0  0   0]

    # After (2,0): value + up
    # [ 0  2  4  54]
    # [ 3  4  5 154]
    # [ 7  0  0   0]

    # After (2,1): value + max(up,left)
    # [ 0  2  4  54]
    # [ 3  4  5 154]
    # [ 7 11  0   0]

    # After (2,2): value + max(up,left)
    # [ 0  2  4  54]
    # [ 3  4  5 154]
    # [ 7 11 13   0]

    # Final state (2,3): value + max(up,left)
    # [ 0  2  4  54]
    # [ 3  4  5 154]
    # [ 7 11 13 154]

    # Result: 154

    
    return dp[m-1][n-1]