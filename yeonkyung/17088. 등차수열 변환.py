import sys
N = int(input())
B = list(map(int, input().split()))

answer = sys.maxsize
changed = False

if N <= 2:
    print(0)
else:
    tmp = []
    for n in [-1, 0, 1]:
        for m in [-1, 0, 1]:
            first = B[0] + n
            second = B[1] + m
            # print(first, second)
            diff = first - second
            if second - diff in [B[2] + i for i in [-1, 0, 1]]:
                tmp.append((n, m))

    if not tmp:
        print(-1)
    else:
        for e in tmp:
            count = 0
            result = [0] * len(B)
            result[0] = B[0] + e[0]
            if e[0] != 0:
                count += 1
            result[1] = B[1] + e[1]
            if e[1] != 0:
                count += 1
            diff = result[0] - result[1]
            i = 2
            while i < len(result):
                if result[i-1] - diff == B[i] + 1:
                    result[i] = B[i] + 1
                    count += 1
                    i += 1
                elif result[i-1] - diff == B[i] - 1:
                    result[i] = B[i] - 1
                    count += 1
                    i += 1
                elif result[i-1] - diff == B[i]:
                    result[i] = B[i]
                    i += 1
                else:
                    break

            if i == len(result):
                changed = True
                answer = min(answer, count)
        if changed:
            print(answer)
        else:
            print(-1)

'''
import sys

def dfs(idx, last, diff, count):
    global answer, flag

    if idx == N:
        flag = True
        answer = min(count, answer)
        return

    for n in [-1, 0, 1]:
        if diff is None or (diff is not None and B[idx] + n - last == diff):
            if n != 0:
                dfs(idx + 1, B[idx] + n, B[idx] + n - last, count + 1)
            else:
                dfs(idx + 1, B[idx] + n, B[idx] + n - last, count)

if __name__ == "__main__":
    N = int(input())
    B = list(map(int, input().split()))

    flag = False
    answer = sys.maxsize
    for n in [-1, 0, 1]:
        if n != 0:
            dfs(1, B[0] + n, None, 1)
        else:
            dfs(1, B[0] + n, None, 0)

    if flag:
        print(answer)
    else:
        print(-1)
'''

