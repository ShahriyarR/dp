def coin_change_exactly_t_coins(n: int, t: int, coins: list[int]) -> int:
    """
    Problem:
	Coin change

	Given an unlimited supply of coins of given denominations,
	find the total number of ways to make a change of size n, by
	using excatly t coins.

	f(i,t) = f(i-1, t-1) + f(i-2, t-1) + f(i-3, t-1) + f(i-5, t-1)
    """

    dp = [[0] * (t+1) for _ in range(n+1)]

    dp[0][0] = 1

    for i in range(n + 1):
        for j in range(t + 1):
            if i > 0 and j == 0:
                dp[i][j] = 0
                continue

            # if i >= 1 {
			# 	dp[i][j] += dp[i-1][j-1]
			# }
			
			# if i >= 2 {
			# 	dp[i][j] += dp[i-2][j-1]
			# }
			
			# if i >= 3 {
			# 	dp[i][j] += dp[i-3][j-1]
			# }
			
			# if i >= 5 {
			# 	dp[i][j] += dp[i-5][j-1]
			# }

            for coin in coins:
                if i - coin >= 0:
                    dp[i][j] += dp[i-coin][j-1]

    return dp[n][t]