N = int(input())
B = list(map(int, input().split()))

dic = dict()
for e in B:
    dic[e] = (e * 2, e // 3 if e % 3 == 0 else None)
# print(dic)

def dfs(idx, n):
    if idx == N:
        print(' '.join(map(str, res)))
        return

    for m in dic[n]:
        if m is not None and m in dic:
            res.append(m)
            tmp = dic[n]
            dic.pop(n)
            dfs(idx+1, m)
            res.pop()
            dic[n] = tmp

for e in B:
    res = [e]
    dfs(1, e)
