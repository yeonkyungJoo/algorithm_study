def solution(number, k):
    stack = []
    for n in list(number):
        n = int(n)

        while stack:
            if k == 0:
                break
            if stack[-1] < n:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(n)

    while k > 0:
        stack.pop()
        k -= 1

    return ''.join(map(str, stack))

if __name__ == "__main__":
    number = "44"
    k = 1
    print(solution(number, k))