'''
def solution(n, computers):
    temp = []
    for i in range(n):
        temp.append(i)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]
    return len(set(temp))
'''

def solution(n, computers):
    count = 0

    def dfs(idx):
        for i in range(len(computers[idx])):
            if i == idx:
                computers[idx][i] = 0
                continue

            if computers[idx][i] == 1:
                computers[idx][i] = 0
                computers[i][idx] = 0
                dfs(i)

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                dfs(i)
                count += 1

    return count

if __name__ == "__main__":
    n = 3
    computers =	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(solution(n, computers))