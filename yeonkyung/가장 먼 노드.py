'''
def solution(n, edge):
    graph = [[50001 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, len(graph)):
        graph[i][i] = 1

    for e1, e2 in edge:
        graph[e1][e2] = 1
        graph[e2][e1] = 1

    for k in range(1, n+1):
        for i in range(1, len(graph)):
            for j in range(1, len(graph)):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph[1].count(max(graph[1][1:]))
'''
from collections import deque
def solution(n, edge):

    dic = dict()
    for e1, e2 in edge:
        if e1 not in dic:
            dic[e1] = []
        if e2 not in dic:
            dic[e2] = []

        dic[e1].append(e2)
        dic[e2].append(e1)

    nodes = [0 for _ in range(n+1)]
    ch = [0 for _ in range(n+1)]
    queue = deque()
    queue.append(1)
    ch[1] = 1
    while queue:
        v = queue.popleft()
        for n in dic[v]:
            if ch[n] == 0:
                queue.append(n)
                ch[n] = 1
                nodes[n] = nodes[v] + 1

    return nodes.count(max(nodes))

if __name__ == "__main__":
    n = 6
    edge = 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, edge))