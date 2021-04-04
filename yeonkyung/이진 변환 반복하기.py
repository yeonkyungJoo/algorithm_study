def binary(n):
    if n == 0:
        return ""
    return binary(n//2) + str(n%2)

def solution(s):
    answer = [0, 0]

    while True:
        if s == "1":
            break

        count = 0
        for e in s:
            if e == "0":
                count += 1
        answer[1] += count
        length = len(s) - count
        s = binary(length)
        answer[0] += 1

    return answer

if __name__ == "__main__":
    s = "1111111"
    print(solution(s))