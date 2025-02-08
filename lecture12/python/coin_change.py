

def coin_change(n: int) -> int:
    """
    Problem:
	Coin change

	Given an unlimited supply of coins of given denominations,
	find the total number of ways to make a change of size n.

	Transition function: f(n) = f(n-d_1) + f(n-d_2) + f(n-d_3) + ... + f(n-d_k),
	where d_1, d_2, d_3, ..., d_k are provided coin denomations.

    Example: we have 1, 3, 5 and 10 cents
    Then the transition function: f(n) = f(n-1) + f(n-2) + f(n-3) + ... + f(n-4)
    """
    # coin_change(4)
    dp = [0] * (n + 1)

    dp[0] = 1

    for i in range(1, n + 1):
        if i >= 1:
            dp[i] += dp[i-1]
        
        if i >= 3:
            dp[i] += dp[i-3]
        
        if i >= 5:
            dp[i] += dp[i-5]
        
        if i >= 10:
            dp[i] += dp[i-10]
    
    return dp[n]


def coin_change_with_denominations(n: int, coins: list[int]) -> int:

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] += dp[i-coin]

    return dp[n]