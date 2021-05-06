def dfs(idx, start):
    global answer

    if idx == M:
        # print([i for i in range(len(chicken_house)) if ch[i] == 1])
        distance = [0] * len(house)
        for i in range(len(house)):
            x1, y1 = house[i][0], house[i][1]
            min_distance = sys.maxsize
            for j in range(len(chicken_house)):
                if ch[j] == 1:
                    x2, y2 = chicken_house[j][0], chicken_house[j][1]
                    min_distance = min(min_distance, abs(x1 - x2) + abs(y1 - y2))
            distance[i] = min_distance
        answer = min(answer, sum(distance))
        return

    for i in range(start, len(chicken_house)):
        if ch[i] == 0:
            ch[i] = 1
            dfs(idx + 1, i)
            ch[i] = 0


if __name__ == "__main__":
    import sys
    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    # print(graph)

    house = []
    chicken_house = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                house.append((i, j))
            if graph[i][j] == 2:
                chicken_house.append((i, j))
    # print(house)
    # print(chicken_house)

    answer = sys.maxsize
    ch = [0] * len(chicken_house)
    dfs(0, 0)
    print(answer)
