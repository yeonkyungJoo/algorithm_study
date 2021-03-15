def solution(n):
    answer = []
    dic = {
        1 : '1',
        2 : '2',
        0 : '4'
    }

    while n > 2:
        remainder = n % 3
        answer.append(dic[remainder])
        n = n // 3
        if remainder == 0:
            n = n - 1

    if n != 0:
        answer.append(dic[n])

    return ''.join(list(reversed(answer)))

if __name__ == "__main__":
    n = 3
    print(solution(n))