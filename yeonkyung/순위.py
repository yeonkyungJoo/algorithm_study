def solution(n, results):

    rank = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for w, l in results:
        rank[w][l] += 1
        rank[l][w] -= 1

    for i in range(1, n+1):
        rank[i][i] = 1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                # 승패를 모르면
                if rank[i][j] == 0:
                    if rank[i][k] == 1 and rank[k][j] == 1:
                        rank[i][j] = 1
                    elif rank[i][k] == -1 and rank[k][j] == -1:
                        rank[i][j] = -1
    answer = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if rank[i][j] == 0:
                break
        else:
            answer += 1

    return answer


if __name__ == "__main__":
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, results))