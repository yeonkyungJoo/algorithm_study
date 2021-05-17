if __name__ == "__main__":
    N = int(input())
    dp = [[0 for _ in range(2)] for _ in range(N+1)]

    dp[1][0] = 0
    dp[1][1] = 1
    for i in range(2, N+1):
        for j in range(2):
            if j == 0:
                dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
            elif j == 1:
                dp[i][j] = dp[i-1][j-1]

    print(sum(dp[N]))