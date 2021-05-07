N, M = map(int, input().split())

nums = [1, 5, 10, 50]
res = set()
def dfs(idx, start, total):
    if idx == N:
        res.add(total)
        return

    for i in range(start, len(nums)):
        dfs(idx+1, i, total + nums[i])

dfs(0, 0, 0)
print(len(res))