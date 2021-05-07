def solution(n, t, m, p):
    answer = ''
    result = ['0']
    for i in range(1, t*m):
        result.append(change(i, n))
    result = ''.join(result)

    i = p-1
    while len(answer) < t:
        answer += result[i]
        i += m
    return answer

def change(n, base):
    if n == 0:
        return ''

    if n % base >= 10:
        remainder = chr(ord('A') + (n % base) - 10)
    else:
        remainder = str(n % base)
    return change(n // base, base) + remainder

if __name__ == "__main__":
    n, t, m, p = 16, 16, 2, 2
    print(solution(n, t, m, p))