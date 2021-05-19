def solution(land):
    N = len(land)
    dp = [[0 for _ in range(0, 4)] for _ in range(N)]

    dp[0] = land[0]
    for i in range(1, N):
        for j in range(0, 4):
            dp[i][j] = max(dp[i-1][0:j] + dp[i-1][j+1:4]) + land[i][j]

    return max(dp[-1])

if __name__ == "__main__":
    land = [[1,2,3,5],
            [5,6,7,8],
            [4,3,2,1]]
    print(solution(land))