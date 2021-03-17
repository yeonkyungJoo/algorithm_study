def solution(numbers, target):
    count = 0

    def dfs(index, res):
        nonlocal count

        if index == len(res):
            answer = 0
            for i in range(len(res)):
                answer += numbers[i] * res[i]
            if answer == target:
                count += 1
            return

        res[index] = 1
        dfs(index + 1, res)
        res[index] = -1
        dfs(index + 1, res)

    res = [0] * len(numbers)
    dfs(0, res)
    return count


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target))
