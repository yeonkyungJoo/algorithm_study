if __name__ == "__main__":
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(list(map(int, input().split())))
    # print(nums)

    dp = [[0 for _ in range(n)] for _ in range(n)]

    dp[0][0] = nums[0][0]
    for i in range(1, len(nums)):
        for j in range(len(nums[i])):
            for x, y in [(1, 0), (1, 1)]:
                if 0 <= i-x < len(nums) and 0 <= j-y < len(nums[i]):
                    dp[i][j] = max(dp[i][j], dp[i-x][j-y] + nums[i][j])

    print(max(dp[-1]))