def solution(n, results):

    rank = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for w, l in results:
        rank[w][l] += 1

    for i in range(1, n+1):
        rank[i][i] = 1
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                rank[i][j] = 1 if rank[i][k] == 1 and rank[k][j] == 1 else rank[i][j]

    order = []
    for i in range(1, n+1):
        total = 0
        for j in range(1, n+1):
            total += rank[j][i]
        order.append((i, total))
    order.sort(key=lambda x : -x[1])

    answer = 0
    cnt = n
    for o in order:
        if o[1] == cnt:
            answer += 1
            cnt -= 1
        else:
            break
    return answer


if __name__ == "__main__":
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, results))