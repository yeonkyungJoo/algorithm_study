import sys
sys.stdin = open("input.txt", "rt")

def dfs(idx, result):
    global count

    if idx == M:
        #print(list(map(str, result)))
        print(' '.join(list(map(str, result))))
        count += 1
        return

    for i in range(N):
        if ch[i] == 0:
            result[idx] = i+1
            for j in range(i+1):
                ch[j] = 1
            dfs(idx+1, result)
            for j in range(i+1):
                ch[j] = 0
            # ch[i] = 0

if __name__ == "__main__":
    N, M = map(int, input().split())
    ch = [0] * N
    result = [0] * M
    count = 0
    #print(N, M)
    dfs(0, result)
    print(count)