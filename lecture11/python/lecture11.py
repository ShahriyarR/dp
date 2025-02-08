def fib(n: int) -> int:
    # this is NOT dynamic programming, but a regular recursion
    if n == 0:
        return 0
    
    if n <= 2:
        return 1
    
    return fib(n-1) + fib(n-2)


def fib_top_down_helper(n: int, memo: dict[int, int]):
    if n == 0:
        return 0
    
    if n <= 2:
        return 1

    if n in memo:
        return memo[n]    

    memo[n] = fib_top_down_helper(n-1, memo) + fib_top_down_helper(n-2, memo)
    return memo[n]


def fib_top_down(n: int) -> int:
    # this is a top-down dynamic programming (a.k.a. recursion + memoization)
    memo = {}
    return fib_top_down_helper(n, memo)


def fib_bottom_up_dp_forward(n: int) -> int:
    """

    this is a bottom-up dynamic programming (forward dynamic programming)

    f(i-1)
        \
        >-------> f(i)
        /
    f(i-2)
    """

    if n == 0:
        return 0
    
    if n <= 2:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]


def fib_bottom_up_dp_backward(n: int) -> int:
    """
     this is a bottom-up dynamic programming (backward dynamic programming)
    
       -----> f(i+2)
       |
     f(i)
       |
       -----> f(i+1)
    
    """

    if n == 0:
        return 0
    
    if n <= 2:
        return 1
    
    dp = [0] * (n + 2) # the reason it contributes to 2 subproblems
    dp[0] = 0
    dp[1] = 1

    for i in range(1, n):
        dp[i+1] += dp[i] # dp[i] is already solved, use it to solve other subproblems
        dp[i+2] += dp[i]

    # Below the state representation of the dp:
    
    # Initial: dp = [0, 1, 0, 0, 0, 0, 0]

    # i=1:
    # dp[2] += dp[1]  # 0+1 = 1
    # dp[3] += dp[1]  # 0+1 = 1
    # [0, 1, 1, 1, 0, 0, 0]

    # i=2:
    # dp[3] += dp[2]  # 1+1 = 2
    # dp[4] += dp[2]  # 0+1 = 1
    # [0, 1, 1, 2, 1, 0, 0]

    # i=3:
    # dp[4] += dp[3]  # 1+2 = 3
    # dp[5] += dp[3]  # 0+2 = 2
    # [0, 1, 1, 2, 3, 2, 0]

    # i=4:
    # dp[5] += dp[4]  # 2+3 = 5
    # dp[6] += dp[4]  # 0+3 = 3
    # [0, 1, 1, 2, 3, 5, 3]

    # i=5:
    # dp[6] += dp[5]  # 3+5 = 8
    # dp[7] += dp[5]  # 0+5 = 5
    # [0, 1, 1, 2, 3, 5, 8]

    # Result: dp[5] = 5

    return dp[n]

