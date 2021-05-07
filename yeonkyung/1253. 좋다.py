N = int(input())
nums = list(map(int, input().split()))
# print(N, nums)

nums.sort()
count = 0
i = 0
while i < len(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        if l == i:
            l += 1
            continue

        if r == i:
            r -= 1
            continue

        if nums[l] + nums[r] == nums[i]:
            count += 1
            break
        elif nums[l] + nums[r] < nums[i]:
            l += 1
        else:
            r -= 1
    i += 1
print(count)