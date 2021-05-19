if __name__ == "__main__":
    import math

    N = int(input())
    dp = [n for n in range(N+1)]

    for i in range(2, (int)(math.sqrt(N) + 1)):
        for j in range(i**2, N+1):
            if j == i**2:
                dp[j] = 1
            else:
                dp[j] = min(dp[j], dp[j-i**2] + 1)

    print(dp[N])