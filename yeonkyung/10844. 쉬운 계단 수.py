if __name__ == "__main__":
    N = int(input())

    dp = [[0 for _ in range(N+1)] for _ in range(10)]
    dp[0][1] = 0
    for i in range(1, 10):
        dp[i][1] = 1

    for i in range(2, N + 1):
        for j in range(0, 10):
            if j == 0:
                dp[j][i] = dp[j+1][i-1]
            elif j == 9:
                dp[j][i] = dp[j-1][i-1]
            else:
                dp[j][i] = (dp[j-1][i-1] + dp[j+1][i-1])

    answer = 0
    for i in range(0, 10):
        answer += dp[i][N]
    print(answer % 1000000000)