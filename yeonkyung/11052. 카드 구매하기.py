if __name__ == "__main__":
    N = int(input())
    price = list(map(int, input().split()))

    dp = [0 for _ in range(N+1)]
    for i in range(N):
        for j in range(i+1, N+1):
            dp[j] = max(dp[j], dp[j-(i+1)] + price[i])
    print(dp[N])