from collections import defaultdict
from collections import deque

def solution(N, road, K):

    nodes = defaultdict(list)
    for s, d, di in road:
        nodes[s].append((d, di))
        nodes[d].append((s, di))
    dist = { i:float('inf') if i != 1 else 0 for i in range(1, N+1) }

    queue = deque([1])
    while queue:
        cur = queue.popleft()
        for next, di in nodes[cur]:
            if dist[next] > dist[cur] + di:
                dist[next] = dist[cur] + di
                queue.append(next)

    return len([True for dist in dist.values() if dist <= K])

if __name__ == "__main__":
    N = 5
    road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
    K = 3
    print(solution(N, road, K))