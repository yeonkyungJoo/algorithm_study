import math

def solution(brown, yellow):
    total = brown + yellow

    r = 1
    while r <= math.sqrt(total):
        if total % r == 0:
            c = total // r

            if (r-2) * (c-2) == yellow and (r+c) * 2 - 4 == brown:
                answer = [c, r]
                break
        r += 1
    return answer

if __name__ == "__main__":
    brown, yellow = 24, 24
    print(solution(brown, yellow))