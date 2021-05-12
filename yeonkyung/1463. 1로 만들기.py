if __name__ == "__main__":
    N = int(input())
    dp = [0] * (N+1)

    for i in range(2, N+1):
        v = dp[i-1]
        if i % 2 == 0:
            v = min(v, dp[i//2])
        if i % 3 == 0:
            v = min(v, dp[i//3])
        dp[i] = v + 1

    print(dp[N])
