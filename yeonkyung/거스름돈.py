def solution(n, money):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1

    for m in money:
        for i in range(m, n+1):
            dp[i] = dp[i] + dp[i-m]

    return dp[n] % 1000000007

if __name__ == "__main__":
    n = 5
    money = [1, 2, 5]
    print(solution(n, money))