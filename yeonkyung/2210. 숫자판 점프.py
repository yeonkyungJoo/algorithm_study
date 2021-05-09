def dfs(idx, x, y, r):
    if idx == 6:
        result.add(r)
        return

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < 5 and 0 <= yy < 5:
            dfs(idx+1, xx, yy, r + str(nums[x][y]))

if __name__ == "__main__":
    nums = []
    for _ in range(5):
        nums.append(list(map(int, input().split())))

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    result = set()

    for i in range(len(nums)):
        for j in range(len(nums[i])):
            dfs(0, i, j, '')
    # print(result)
    print(len(result))