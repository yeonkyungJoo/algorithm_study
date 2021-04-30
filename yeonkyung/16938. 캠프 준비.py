N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))

ch = [0] * len(A)
answer = 0
A.sort()

def dfs(idx, start, diff, total):

    global answer

    if L <= total <= R and diff >= X:
        answer += 1

    if idx == N:
        return

    for i in range(start, len(A)):
        if ch[i] == 0:
            ch[i] = 1
            easy = 0
            for j, k in enumerate(ch):
                if k == 1:
                    easy = j
                    break
            dfs(idx + 1, i + 1, A[i] - A[easy], total + A[i])
            ch[i] = 0


dfs(0, 0, 0, 0)
print(answer)
