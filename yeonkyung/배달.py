'''
# 시간 초과
def solution(N, road, K):

    dir = dict()
    for a, b, c in road:
        if a not in dir:
            dir[a] = []
        if b not in dir:
            dir[b] = []

        dir[a].append((b, c))
        dir[b].append((a, c))

    for k, v in dir.items():
        print(k, v)

    ch = [0 for _ in range(N+1)]
    answer = set()
    def dfs(e, total):

        if total <= K:
            answer.add(e)
        if total > K:
            return

        for i, j in dir[e]:
            if ch[i] == 0:
                ch[i] = 1
                dfs(i, total + j)
                ch[i] = 0

    ch[1] = 1
    dfs(1, 0)
    return len(answer)
'''

def solution(N, road, K):
    answer = 0
    dis = [[500001 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(1, len(dis)):
        dis[i][i] = 0

    for r in road:
        v1, v2, t = r[0], r[1], r[2]
        dis[v1][v2] = min(dis[v1][v2], t)
        dis[v2][v1] = min(dis[v2][v1], t)

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    for i in range(1, N+1):
        if dis[1][i] <= K:
            answer += 1

    return answer

if __name__ == "__main__":
    N = 6
    road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
    K = 4
    print(solution(N, road, K))