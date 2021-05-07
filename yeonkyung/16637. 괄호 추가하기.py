import sys

def dfs(idx, total):
    global answer

    if idx >= N:
        answer = max(int(total), answer)
        return

    first = str(eval(total + exp[idx] + exp[idx+1]))
    dfs(idx + 2, first)
    if idx + 3 < N:
        second = str(eval(total + exp[idx] + str(eval(exp[idx+1] + exp[idx+2] + exp[idx+3]))))
        dfs(idx + 4, second)


if __name__ == "__main__":
    N = int(input())
    exp = list(input())
    answer = -sys.maxsize
    dfs(1, exp[0])
    print(answer)
