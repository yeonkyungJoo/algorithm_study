'''
def solution(n, k):
    answer = []
    ch = [0 for _ in range(n+1)]

    def dfs(idx, order):
        if idx == n:
            answer.append(order[:])
            return

        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                order.append(i)
                dfs(idx+1, order)
                order.pop()
                ch[i] = 0
    dfs(0, [])
    return answer[k-1]
'''

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    return n * factorial(n-1)

def solution(n, k):

    numbers = [i for i in range(1, n+1)]
    answer = [0 for _ in range(n)]
    idx = 0
    j = 0
    while k >= 0:
        if idx == n-1:
            break
        length = n - idx - 1
        f = factorial(length)
        if k - f > 0:
            k -= f
            j += 1
        else:
            answer[idx] = numbers.pop(j)
            j = 0
            idx += 1

    answer[-1] = numbers.pop()
    return answer

if __name__ == "__main__":
    n, k = 4, 24
    print(solution(n, k))