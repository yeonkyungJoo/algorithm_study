def solution(n):
    count = 0
    i = 1
    while n - (i*(i-1)//2) > 0:
        if (n - (i*(i-1)//2)) % i == 0:
            count += 1
        i += 1

    return count

if __name__ == "__main__":
    n = 15
    print(solution(n))