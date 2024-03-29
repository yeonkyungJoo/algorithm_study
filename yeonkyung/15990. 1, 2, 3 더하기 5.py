if __name__ == "__main__":
    '''
    import sys
    input = sys.stdin.readline
    '''
    dp = [[0 for _ in range(100001)] for _ in range(4)]
    dp[1][1] = 1
    dp[2][2] = 1
    dp[1][3] = 1
    dp[2][3] = 1
    dp[3][3] = 1

    for i in range(4, 100001):
        dp[1][i] = (dp[2][i - 1] + dp[3][i - 1]) % 1000000009
        dp[2][i] = (dp[1][i - 2] + dp[3][i - 2]) % 1000000009
        dp[3][i] = (dp[1][i - 3] + dp[2][i - 3]) % 1000000009

    T = int(input())
    for _ in range(T):
        n = int(input())
        print((dp[1][n] + dp[2][n] + dp[3][n]) % 1000000009)