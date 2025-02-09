def coin_change_no_more_than_t_coins(n: int, t: int, coins: list[int]) -> int:
    dp = [[0] * (t+1) for _ in range(n+1)]

    dp[0][0] = 1

    for i in range(n + 1):
        for j in range(t + 1):
            if i > 0 and j == 0:
                dp[i][j] = 0
                continue

            if i == 0 and j > 0:
                dp[i][j] = 1
                continue

            for coin in coins:
                if i - coin >= 0:
                    dp[i][j] += dp[i-coin][j-1]

    return dp[n][t]