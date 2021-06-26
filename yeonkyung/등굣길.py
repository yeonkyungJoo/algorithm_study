def solution(m, n, puddles):
    road = [[0 for _ in range(m)] for _ in range(n)]
    for puddle in puddles:
        x, y = puddle[1], puddle[0]
        road[x-1][y-1] = -1

    for i in range(1, n):
        if road[i][0] == -1:
            break
        else:
            road[i][0] = 1

    for i in range(1, m):
        if road[0][i] == -1:
            break
        else:
            road[0][i] = 1

    for i in range(1, n):
        for j in range(1, m):
            if road[i][j] == -1:
                continue
            road[i][j] = ((0 if road[i-1][j] == -1 else road[i-1][j]) + (0 if road[i][j-1] == -1 else road[i][j-1])) % 1000000007

    return road[n-1][m-1]

if __name__ == "__main__":
    m, n = 4, 3
    puddles = [[2, 2]]
    print(solution(m, n, puddles))