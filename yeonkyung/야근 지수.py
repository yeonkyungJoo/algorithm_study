import heapq

def solution(n, works):

    works = [w * (-1) for w in works]
    heapq.heapify(works)

    for _ in range(n):
        work = heapq.heappop(works) * (-1)
        if work == 0:
            break
        heapq.heappush(works, (work - 1) * (-1))

    return sum([(w * (-1)) ** 2 for w in works])

if __name__ == "__main__":
    n, works = 1, [2, 1, 2]
    print(solution(n, works))