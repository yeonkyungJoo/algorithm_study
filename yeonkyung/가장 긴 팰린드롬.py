'''
def solution(s):

    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

    for i in range(len(s)):

        start, end = i, i
        dp[start][end] = 1

        while True:
            if start-1 >= 0 and end+1 <= len(s)-1 and s[start-1] == s[end+1]:
                dp[start-1][end+1] = max(dp[start][end] + 2, dp[start-1][end+1])
                start -= 1
                end += 1
            elif start-1 >= 0 and end <= len(s)-1 and s[start-1] == s[end]:
                dp[start-1][end] = max(dp[start][end] + 1, dp[start-1][end])
                start -= 1
            elif start >= 0 and end + 1 <= len(s)-1 and s[start] == s[end+1]:
                dp[start][end+1] = max(dp[start][end] + 1, dp[start][end+1])
                end += 1
            else:
                break

    answer = 0
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            answer = max(answer, dp[i][j])
    return answer
'''
def solution(s):
    answer = 1
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                answer = max(answer, len(s[i:j]))
    return answer

if __name__ == "__main__":
    s = "abcdcba"
    print(solution(s))