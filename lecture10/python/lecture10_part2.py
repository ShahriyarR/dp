
def num_ways(n: int) -> int:
    """
    Paint Fence With Two Colors

	There is a fence with n posts, each post can be painted with either green or blue color.
	You have to paint all the posts such that no more than two adjacent fence posts have the same color.
	Return the total number of ways you can paint the fence.

    Transition function:
    f(i, j) = f(i-1, 1-j) + f(i-2, 1-j)
    """

    dp = [[0] * 2 for _ in range(n+1)]

    # green = 1
    # blue = 0

    dp[1][0] = 1
    dp[1][1] = 1

    # if we have 2 posts, then we have 2 ways of coloring
    dp[2][0] = 2 # first blue, second green or first blue and second blue 10, 00 
    dp[2][1] = 2 # first green, second blue or first green and second green 01, 11

    for i in range(3, n + 1): # start from 3 as we have already covered the base cases above
        for j in range(0, 2): # as we have 2 colors
            dp[i][j] = dp[i-1][1-j] + dp[i-2][1-j]

    # Simplified representation:

    # dp[i][j] where i = post number, j = color (0=blue, 1=green)

    # Initial state:
    # Post 1: [1, 1]   # One way each for blue(0) and green(1)
    # Post 2: [2, 2]   # Two ways each
    # Post 3:
    # dp[3][0] = dp[2][1] + dp[1][1] = 2 + 1 = 3
    # dp[3][1] = dp[2][0] + dp[1][0] = 2 + 1 = 3
    # [3, 3]

    # Post 4:
    # dp[4][0] = dp[3][1] + dp[2][1] = 3 + 2 = 5
    # dp[4][1] = dp[3][0] + dp[2][0] = 3 + 2 = 5
    # [5, 5]

    # Post 5:
    # dp[5][0] = dp[4][1] + dp[3][1] = 5 + 3 = 8
    # dp[5][1] = dp[4][0] + dp[3][0] = 5 + 3 = 8
    # [8, 8]

    # Final result = dp[5][0] + dp[5][1] = 8 + 8 = 16
    
    # FULL The representation of the states:

    # Key: B = Blue (0), G = Green (1)
    # Post 1: [1, 1]
    # |B| or |G|

    # Post 2: [2, 2]
    # |B|B| or |B|G| or |G|B| or |G|G|

    # Post 3: [3, 3]
    # For Blue end (dp[3][0]):
    # |G|G|B|
    # |G|B|B|
    # |B|G|B|

    # For Green end (dp[3][1]):
    # |B|B|G|
    # |B|G|G|
    # |G|B|G|

    # Post 4: [5, 5]
    # For Blue end (dp[4][0]):
    # |B|G|G|B|
    # |G|B|G|B|
    # |G|G|B|B|
    # |B|B|G|B|
    # |B|G|B|B|

    # For Green end (dp[4][1]):
    # Similar pattern with G at end

    # Post 5: [8, 8]
    # For Blue end (dp[5][0]):
    # |B|G|G|B|B|
    # |G|B|G|B|B|
    # |G|G|B|B|B|
    # |B|B|G|B|B|
    # |B|G|B|B|B|
    # |G|B|B|G|B|
    # |B|G|B|G|B|
    # |G|B|G|G|B|

    # For Green end (dp[5][1]):
    # Similar pattern with G at end

    # Total ways = 16
    
    # As we need the total numbers of the ways:
    # first we get the value if the last post was blue
    # then add if the last post was green
    return dp[n][0] + dp[n][1]