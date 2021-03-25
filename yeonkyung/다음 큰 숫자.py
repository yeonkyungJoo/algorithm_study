import math
import sys

def solution(n):

    def count_one(n):
        cnt = 0
        while n > 0:
            if n % 2 == 1:
                cnt += 1
            n = n // 2
        return cnt

    '''
    answer = sys.maxsize
    def dfs(idx, cnt, sum):
        nonlocal answer

        if idx > total + 1:
            return
        if cnt == count:
            if sum > n:
                answer = min(answer, sum)
            return

        dfs(idx + 1, cnt + 1, sum + math.pow(2, idx))
        dfs(idx + 1, cnt, sum)

    dfs(0, 0, 0)
    '''

    count = count_one(n)
    for i in range(n+1, 1000001):
        if count == count_one(i):
            answer = i
            break
    return answer


if __name__ == "__main__":
    n = 78
    print(solution(n))