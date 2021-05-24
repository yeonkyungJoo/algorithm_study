if __name__ == "__main__":
    N = int(input())
    dp = [0 for _ in range(N+1)]

    dp[0] = 1
    dp[1] = 3

    for i in range(2, N+1):
        dp[i] = dp[i-1] * 2 + dp[i-2]

    print(dp[N] % 9901)


