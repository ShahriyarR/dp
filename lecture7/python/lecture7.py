def paid_stair_case(n: int, p: list[int]) -> int:
    """
Problem:
	Paid Staircase

	You are climbing a paid staircase. It takes n steps to reach to the top and you have to
	pay p[i] to step on the i-th stair. Each time you can climb 1 or 2 steps.
	What's the cheapest amount you have to pay to get to the top of the staircase?


Time complexity: O(n)
Space complexity: O(n)
    """

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = p[1]

    for i in range(2, n + 1):
        dp[i] = p[i] + min(dp[i-1], dp[i-2])

    return dp[n] 