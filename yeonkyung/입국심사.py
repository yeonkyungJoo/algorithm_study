def solution(n, times):
    left = 0
    answer = right = max(times) * n

    while left <= right:
        task_sum = 0
        mid = (left + right) // 2

        for time in times:
            task_sum += mid // time

        if task_sum < n:
            left = mid + 1
        else:
            right = mid - 1
            if mid <= answer:
                answer = mid

    return answer

if __name__ == "__main__":
    n, times = 6, [7, 10]
    print(solution(n, times))