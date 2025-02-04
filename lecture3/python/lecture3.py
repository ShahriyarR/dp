# Python implementation of the Lecture 3 code

def n_sum(n: int) -> int:
   """
    Problem:
	    Find the sum of the first N numbers.

    Objective function:
        f(i) is the sum of the first i elements.

    Recurrence relation:
        f(n) = f(n-1) + n
   """
   # For example, for n = 5, the array will look like: [None, None, None, None, None, None]
   dp =[None] * (n + 1)
   # After this assignment it will look like: [0, None, None, None, None, None]
   dp[0] = 0

   # The for loop below for n = 5:

#    dp[5] = dp[4] + 5
#     ├── dp[4] = dp[3] + 4
#     │   ├── dp[3] = dp[2] + 3
#     │   │   ├── dp[2] = dp[1] + 2
#     │   │   │   ├── dp[1] = dp[0] + 1
#     │   │   │   │   └── dp[0] = 0
#     │   │   │   └── result: 1
#     │   │   └── result: 3
#     │   └── result: 6
#     └── result: 10
# └── final result: 15
   
   for index in range(1, n + 1):
    dp[index] = dp[index-1] + index

    # And let's see the array update for each iteration:

    # Initial: [0, None, None, None, None, None]
    # dp[1] = dp[0] + 1
    # └── [0, 1, None, None, None, None]

    # dp[2] = dp[1] + 2
    # └── [0, 1, 3, None, None, None]

    # dp[3] = dp[2] + 3
    # └── [0, 1, 3, 6, None, None]

    # dp[4] = dp[3] + 4
    # └── [0, 1, 3, 6, 10, None]

    # dp[5] = dp[4] + 5
    # └── [0, 1, 3, 6, 10, 15]
   
   # n'th element of the array will hold the final sum, so basically, we just return dp[5], which is 15
   return dp[n]
