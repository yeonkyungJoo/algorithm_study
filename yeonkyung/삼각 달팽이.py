def solution(n):

    direction = [(1, 0), (0, 1), (-1, -1)]
    result = [[0 for _ in range(n+1)] for _ in range(n+1)]

    x, y = 0, 0
    j = 0
    m = 1
    for i in range(n, 0, -1):
        for _ in range(i):
            x = x + direction[j][0]
            y = y + direction[j][1]
            result[x][y] = m
            m += 1
        j = (j+1) % 3

    answer = []
    for i in range(len(result)):
        for j in range(len(result[i])):
            if result[i][j] != 0:
                answer.append(result[i][j])
    return answer

if __name__ == "__main__":
    n = 6
    print(solution(n))
