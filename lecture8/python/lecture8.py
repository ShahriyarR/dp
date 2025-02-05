def paid_stair_case(n: int, p: list[int]) -> list[int]:
    """

Problem:
	Paid Staircase II

	You are climbing a paid staircase. It takes n steps to reach to the top and you have to
	pay p[i] to step on the i-th stair. Each time you can climb 1 or 2 steps.
	Return the cheapest path to the top of the staircase.

Template to reconstruct the path
================================

	path = []
	for curr = best_last_state; curr exists; curr = from[curr] {
		path.push(curr)
	}
	return path.reverse()



Time complexity: O(n)
Space complexity: O(n)
    """

    dp = [0] * (n + 1)
    from_ = [0] * (n + 1)

    dp[0] = 0
    dp[1] = p[1]

    for i in range(2, n + 1):
        dp[i] = min(dp[i-1], dp[i-2]) + p[i]

        if dp[i - 1] < dp[i - 2]:
            from_[i] = i - 1
        else:
            from_[i] = i - 2
    
    # For n=8, after running for loop dp is:
    # [0, 3, 2, 6, 8, 7, 8, 12, 11]
    # from_ is:
    # [0, 0, 0, 2, 2, 3, 5, 5, 6]

    
    path = []
    curr = n
    while curr >= 0:
        path.append(curr)
        if curr == 0:
            break
        curr = from_[curr]
    
    # Let's assume that n=8 and from_ as defined below
    
    # from_ = [0, 0, 0, 2, 2, 3, 5, 5, 6]

    # curr = 8, path = [8]
    # curr = 6, path = [8, 6]
    # curr = 5, path = [8, 6, 5]
    # curr = 3, path = [8, 6, 5, 3]
    # curr = 2, path = [8, 6, 5, 3, 2]
    # curr = 0, path = [8, 6, 5, 3, 2, 0]

    # After reverse:
    # path = [0, 2, 3, 5, 6, 8]
    
    return path[::-1] # reverse


if __name__ == "__main__":
    paid_stair_case(8, [0, 3, 2, 4, 6, 1, 1, 5, 3])


