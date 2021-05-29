def solution(n,a,b):
    count = 0

    def recursive(a, b):
        nonlocal count

        count += 1
        if max(a, b) % 2 == 0 and max(a, b) - min(a, b) == 1:
            return

        a = a // 2 if a % 2 == 0 else (a + 1) // 2
        b = b // 2 if b % 2 == 0 else (b + 1) // 2

        recursive(a, b)

    recursive(a, b)
    return count

if __name__ == "__main__":
    n, a, b = 8, 1, 2
    print(solution(n, a, b))