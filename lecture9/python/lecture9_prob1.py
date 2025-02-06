def unique_paths(m: int, n: int) -> int:
    """
    Problem:
	Unique Paths

	A robot is located at the top-left corner of a m x n grid (marked 'S' in the diagram below).
	The robot can only move either down or right at any point in time.
	The robot is trying to reach the bottom-right corner of the grid (marked 'E' in the diagram below).

	How many possible unique paths are there?

	+---+---+---+---+
	| S |   |   |   |
	+---+---+---+---+
	|   |   |   |   |
	+---+---+---+---+
	|   |   |   | E |
	+---+---+---+---+

	Above is a 3 x 4 grid. How many possible unique paths are there?

    Time complexity:
    Space complexity:
    F(i,j) = F(i-1,j) + F(i,j-1)
    """

    dp = [[0] * n for _ in range(m)]

    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if i > 0 and j > 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            elif i > 0:
                dp[i][j] = dp[i-1][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1]

    # Comments below showing each state for the iterations.
    
    # Initial state:
    # [1 0 0 0]
    # [0 0 0 0]
    # [0 0 0 0]

    # After (0,1): first row, j>0
    # [1 1 0 0]
    # [0 0 0 0]
    # [0 0 0 0]

    # After (0,2):
    # [1 1 1 0]
    # [0 0 0 0]
    # [0 0 0 0]

    # After (0,3):
    # [1 1 1 1]
    # [0 0 0 0]
    # [0 0 0 0]

    # After (1,0): first column, i>0
    # [1 1 1 1]
    # [1 0 0 0]
    # [0 0 0 0]

    # After (1,1): i>0 and j>0, sum of up and left
    # [1 1 1 1]
    # [1 2 0 0]
    # [0 0 0 0]

    # After (1,2):
    # [1 1 1 1]
    # [1 2 3 0]
    # [0 0 0 0]

    # After (1,3):
    # [1 1 1 1]
    # [1 2 3 4]
    # [0 0 0 0]

    # After (2,0): first column
    # [1 1 1 1]
    # [1 2 3 4]
    # [1 0 0 0]

    # After (2,1): 
    # [1 1 1 1]
    # [1 2 3 4]
    # [1 3 0 0]

    # After (2,2):
    # [1 1 1 1]
    # [1 2 3 4]
    # [1 3 6 0]

    # Final state (2,3):
    # [1 1 1  1]
    # [1 2 3  4]
    # [1 3 6 10]

    # Result: 10 unique paths

    
    return dp[m-1][n-1]

