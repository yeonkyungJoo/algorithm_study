from collections import deque


def solution(maps):

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    n, m = len(maps), len(maps[0])
    queue = deque()
    ch = [[-1 for _ in range(m)] for _ in range(n)]
    queue.append((0, 0))
    ch[0][0] = 1
    maps[0][0] = 2
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            break
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and maps[xx][yy] == 1:
                queue.append((xx, yy))
                ch[xx][yy] = ch[x][y] + 1
                maps[xx][yy] = 2

    if maps[n - 1][m - 1] == 2:
        answer = ch[n - 1][m - 1]
    else:
        answer = -1
    return answer


if __name__ == "__main__":
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
    print(solution(maps))
