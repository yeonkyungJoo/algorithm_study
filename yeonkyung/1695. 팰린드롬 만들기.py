def recursive(start, end):
    if dp[start][end] != -1:
        return dp[start][end]

    if start == end:
        return 0
    elif start == end - 1:
        if nums[start] == nums[end]:
            return 0
        else:
            return 1

    if nums[start] == nums[end]:
        dp[start][end] = recursive(start + 1, end - 1)
        return dp[start][end]
    else:
        dp[start][end] = min(recursive(start + 1, end), recursive(start, end - 1)) + 1
        return dp[start][end]

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))

    dp = [[-1 for _ in range(N)] for _ in range(N)]
    print(recursive(0, N-1))