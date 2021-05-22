if __name__ == "__main__":
    N, M = map(int, input().split())
    candy = []
    for _ in range(N):
        candy.append(list(map(int, input().split())))
    # print(candy)

    dp = [[0 for _ in range(M)] for _ in range(N)]
    dp[0][0] = candy[0][0]

    for i in range(1, len(candy)):
        dp[i][0] = dp[i-1][0] + candy[i][0]

    for j in range(1, len(candy[0])):
        dp[0][j] = dp[0][j-1] + candy[0][j]

    for i in range(1, len(candy)):
        for j in range(1, len(candy[i])):
            for x, y in [(1, 1), (1, 0), (0, 1)]:
                dp[i][j] = max(dp[i][j], dp[i-x][j-y] + candy[i][j])

    print(dp[N-1][M-1])



