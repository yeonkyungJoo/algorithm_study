'''
#1 - 브루트포스 1
def solution(s):
    answer = 1
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                answer = max(answer, len(s[i:j]))
    return answer

#2 - 브루트포스 2
def solution(s):
    for i in range(len(s), 0, -1):
        for j in range(len(s)-i+1):
            if s[j:j+i] == s[j:j+i][::-1]:
                return i


#3 - 재귀
def solution(s):
    if s == s[::-1]:
        return len(s)
    return max(solution(s[1:], solution(s[:-1])))
'''

#4 - DP(TD)
def solution(s):
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

    def recursive(start, end):

        if dp[start][end] != 0:
            return dp[start][end]

        # 길이가 1
        if start == end:
            dp[start][end] = 1
            return dp[start][end]

        # 길이가 2
        if start+1 == end:
            if s[start] == s[end]:
                dp[start][end] = 1
                return dp[start][end]
            else:
                dp[start][end] = 0
                return dp[start][end]

        # 길이가 3 이상
        if s[start] != s[end]:
            dp[start][end] = 0
            return dp[start][end]

        dp[start][end] = recursive(start+1, end-1)
        return dp[start][end]

    answer = 0
    for i in range(len(s)):
        for j in range(len(s)-1, i-1, -1):

            if recursive(i, j) == 1:
                answer = max(answer, j - i + 1)

    return answer

#5 - DP(BU)
def solution(s):
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

    # 길이가 1
    for i in range(len(s)):
        dp[i][i] = 1

    # 길이가 2
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 1
        else:
            dp[i][i+1] = 0

    # 길이가 3 이상
    for k in range(3, len(s)+1):
        for i in range(len(s)-k+1):
            j = i+k-1

            if s[i] == s[j] and dp[i+1][j-1] == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = 0

    answer = 1
    for i in range(len(s)):
        for j in range(len(s)-1, i-1, -1):
            if dp[i][j] == 1:
                answer = max(answer, j - i + 1)
    return answer

if __name__ == "__main__":
    s = "abcdcba"
    print(solution(s))