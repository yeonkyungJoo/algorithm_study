if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    dp = [0 for _ in range(N)]
    for i in range(N):
        max_length = 0
        for j in range(i-1, -1, -1):
            if A[i] > A[j]:
                max_length = max(max_length, dp[j])
        dp[i] = max_length + 1

    answer = max(dp)
    print(answer)
    result = []
    for i in range(N-1, -1, -1):
        if dp[i] == answer:
            result.append(A[i])
            answer -= 1
    result.reverse()
    print(' '.join(list(map(str, result))))