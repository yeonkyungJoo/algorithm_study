def solution(n):

    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = (dp[i-2] + dp[i-1])

    return dp[n] % 1234567

if __name__ == "__main__":
    n = 2000
    print(solution(n))