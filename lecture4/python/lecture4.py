def climb_stairs(n: int) -> int:

    """
    Problem:
	Climbing Stairs

	You are climbing a stair case. It takes n steps to reach to the top.
	Each time you can either climb 1 or 2 steps.
	In how many distinct ways can you climb to the top?

Framework for Solving DP Problems:
	1. Define the objective function
		f(i) is the number of distinct ways to reach the i-th stair.
	2. Identify base cases
		f(0) = 1
		f(1) = 1
	3. Write down a recurrence relation for the optimized objective function
		f(n) = f(n-1) + f(n-2)
	4. What's the order of execution?
		bottom-up
	5. Where to look for the answer?
		f(n)

    Time complexity: O(n)
    Space complexity: O(n)
    """

    dp = [None] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for index in range(2, n + 1):
        dp[index] = dp[index - 1] + dp[index - 2]

    # Below the commented area shows the steps/states, for n=5.

    # Initial: [1, 1, None, None, None, None]

    # dp[2] = dp[1] + dp[0]
    # └── [1, 1, 2, None, None, None]

    # dp[3] = dp[2] + dp[1]
    # └── [1, 1, 2, 3, None, None]

    # dp[4] = dp[3] + dp[2]
    # └── [1, 1, 2, 3, 5, None]

    # dp[5] = dp[4] + dp[3]
    # └── [1, 1, 2, 3, 5, 8]

    # Ways to reach each step:
    # Step 0: 1 way
    # Step 1: 1 way    (1)
    # Step 2: 2 ways   (1+1, 2)
    # Step 3: 3 ways   (1+1+1, 1+2, 2+1)
    # Step 4: 5 ways   (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)
    # Step 5: 8 ways   (1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 2+2+1, 2+1+2, 1+2+2)
    
    return dp[n]