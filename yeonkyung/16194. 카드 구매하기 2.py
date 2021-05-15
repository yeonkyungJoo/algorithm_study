if __name__ == "__main__":
    N = int(input())
    price = list(map(int, input().split()))

    dp = [0 for _ in range(N+1)]
    for i in range(len(price)):
        for j in range(i+1, N+1):
            if dp[j] == 0:
                dp[j] = dp[j-(i+1)] + price[i]
            else:
                dp[j] = min(dp[j], dp[j-(i+1)] + price[i])
    print(dp[N])