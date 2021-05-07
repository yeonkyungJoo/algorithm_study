import sys

def dfs(idx, start, total):
    if idx == 7:
        if total == 100:
            for i in range(len(ch)):
                if ch[i] == 1:
                    print(height[i])
            sys.exit()

    for i in range(start, len(height)):
        if ch[i] == 0:
            ch[i] = 1
            dfs(idx+1, i, total + height[i])
            ch[i] = 0

if __name__ == "__main__":
    height = []
    for _ in range(9):
        height.append(int(input()))
    height.sort()
    ch = [0] * len(height)
    dfs(0, 0, 0)