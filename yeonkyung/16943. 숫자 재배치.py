A, B = map(int, input().split())

nums = list(str(A))
ch = [0] * len(nums)

answer = -1
res = []
def dfs(idx):
    global answer

    if idx == len(nums):
        if res[0] == '0':
            return
        else:
            C = int(''.join(map(str, res)))
            if C < B:
                answer = max(answer, C)

    for i in range(0, len(nums)):
        if ch[i] == 0:
            ch[i] = 1
            res.append(nums[i])
            dfs(idx+1)
            res.pop()
            ch[i] = 0

dfs(0)
print(answer)
