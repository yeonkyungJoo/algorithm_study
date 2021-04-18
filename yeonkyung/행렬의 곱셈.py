def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]

    list1 = [e for e in arr1]
    list2 = [[] for _ in range(len(arr2[0]))]
    for i in arr2:
        for idx, j in enumerate(i):
            list2[idx].append(j)

    for i in range(len(answer)):
        for j in range(len(answer[0])):
            total = 0
            for k in range(len(list1[i])):
                total += list1[i][k] * list2[j][k]
            answer[i][j] = total
    return answer

if __name__ == "__main__":
    arr1 = [[2, 3, 2],
            [4, 2, 4],
            [3, 1, 4]]
    arr2 = [[5, 4, 3],
            [2, 4, 1],
            [3, 1, 1]]
    print(solution(arr1, arr2))