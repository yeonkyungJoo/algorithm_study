import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n+1)) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    tmp = [-1] * len(numbers)
    ch = [0] * len(numbers)
    answer = []

    def dfs(idx):
        if idx == len(numbers):
            return answer

        for i in range(len(numbers)):
            if ch[i] == 0:
                ch[i] = 1
                tmp[idx] = int(numbers[i])
                answer.append(int(''.join([str(n) for n in tmp if n != -1])))
                dfs(idx + 1)
                ch[i] = 0
                tmp[idx] = -1

    dfs(0)
    count = 0
    for number in set(answer):
        if isPrime(number):
            count += 1
    return count

if __name__ == "__main__":
    numbers = "17"
    print(solution(numbers))