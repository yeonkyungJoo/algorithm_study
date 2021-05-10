def dfs(idx, start, s):
    global count

    if idx == 3:
        n1, n2, n3 = map(int, s.lstrip().split())
        if impossible[n1][n2] != 1 and impossible[n2][n3] != 1 and impossible[n1][n3] != 1:
            count += 1
        return

    for i in range(start+1, N+1):
        if ch[i] == 0:
            ch[i] = 1
            dfs(idx+1, i, s + ' ' + str(i))
            ch[i] = 0

'''
def dfs(idx, start, s):
    global count

    if idx == 3:
        # print(s)
        count += 1
        return

    for i in range(start+1, N+1):
        for j in range(len(impossible[i])):
            if impossible[i][j] == 1:
                ch[j] += 1

        if ch[i] == 0:
            dfs(idx + 1, i, s + str(i))

        for j in range(len(impossible[i])):
            if impossible[i][j] == 1:
                ch[j] -= 1
'''
if __name__ == "__main__":
    N, M = map(int, input().split())
    impossible = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for _ in range(M):
        i, j = map(int, input().split())
        impossible[i][j] += 1
        impossible[j][i] += 1

    count = 0
    ch = [0] * (N+1)
    dfs(0, 0, '')
    print(count)
