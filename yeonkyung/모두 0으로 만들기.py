'''
def solution(a, edges):

    if sum(a) != 0:
        return -1
    if a.count(0) == len(a):
        return 0

    graph = [[0 for _ in range(len(a))] for _ in range(len(a))]
    for edge in edges:
        e1, e2 = edge[0], edge[1]
        graph[e1][e2] = 1
        graph[e2][e1] = 1

    def dfs(idx):
        nonlocal count

        tmp = 0
        for i in range(len(graph[idx])):
            if graph[idx][i] == 1:
                graph[idx][i] = 0
                graph[i][idx] = 0
                v = dfs(i)
                tmp += v
                count += abs(v)

        return tmp + a[idx]

    count = 0
    dfs(0)
    return count
'''
import sys
sys.setrecursionlimit(300000)

def solution(a, edges):

    if sum(a) != 0:
        return -1
    if a.count(0) == len(a):
        return 0

    graph = dict()
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        graph[u].append(v)
        graph[v].append(u)

    count = 0
    def dfs(u, v):
        nonlocal count

        for node in graph[u]:
            if node != v:
                dfs(node, u)

        count += abs(a[u])
        a[v] += a[u]
        a[u] = 0

    dfs(0, 0)
    return count


if __name__ == "__main__":
    a = [-5,0,2,1,2]
    edges = [[0,1],[3,4],[2,3],[0,3]]
    print(solution(a, edges))