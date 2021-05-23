if __name__ == "__main__":
    import sys
    N = int(input())
    A = list(map(int, input().split()))

    dp = [sys.maxsize for _ in range(N)]
    dp[0] = 0
    for i in range(N):
        for j in range(1, A[i]+1):
            if 0 <= i+j < len(A):
                dp[i+j] = min(dp[i]+1, dp[i+j])

    if dp[-1] == sys.maxsize:
        print(-1)
    else:
        print(dp[-1])
