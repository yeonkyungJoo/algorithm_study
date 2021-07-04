def solution(n, s):
    if s // n == 0:
        return [-1]

    answer = [s // n for _ in range(n)]

    r = s % n
    i = 0
    while r > 0:
        answer[i] += 1
        r -= 1
        i += 1

    answer.sort()
    return answer


if __name__ == "__main__":
    n, s = 2, 8
    print(solution(n, s))