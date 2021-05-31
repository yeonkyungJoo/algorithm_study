'''
def solution(n):
    count = 0

    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            count += 1

    return count
'''
def solution(n):
    return bin(n).count('1')

if __name__ == "__main__":
    n = 5000
    print(solution(n))