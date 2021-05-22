def solution(triangle):
    n = len(triangle)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            for x, y in [(1, 0), (1, 1)]:
                if 0 <= i-x < len(triangle) and 0 <= j-y < len(triangle[i]):
                    dp[i][j] = max(dp[i][j], dp[i-x][j-y] + triangle[i][j])

    return max(dp[-1])

if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(triangle))
