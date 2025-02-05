

def climb_stairs_k_steps_skip_red(n: int, k: int, stairs: list[bool]) -> int:
    """
    Problem:
	Climbing Stairs (k steps, space optimized, skip red steps)

	You are climbing a stair case. It takes n steps to reach to the top.
	Each time you can climb 1..k steps. You are not allowed to step on red stairs.
	In how many distinct ways can you climb to the top?


    Time complexity: O(nk)
    Space complexity: O(k)
    """

    dp = [0] * k
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(1, k):
            if i - j < 0:
                continue

            if stairs[i-1]:
                dp[i % k] = 0
            else:
                dp[i % k] += dp[(i-j) % k]

    return dp[n % k]