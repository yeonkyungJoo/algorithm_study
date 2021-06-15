import heapq

def solution(operations):
    min_heap = list()
    max_heap = list()

    insert = 0
    delete = 0
    for operation in operations:
        op, n = operation.split()
        n = int(n)
        if op == 'I':
            insert += 1
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, n * (-1))
        else:
            delete += 1
            if n == -1:
                if len(min_heap) != 0:
                    heapq.heappop(min_heap)
            else:
                if len(max_heap) != 0:
                    heapq.heappop(max_heap)

    if delete >= insert:
        return [0, 0]
    else:
        m = heapq.heappop(min_heap)
        while True:
            if m * (-1) not in max_heap:
                m = heapq.heappop(min_heap)
            else:
                break

        n = heapq.heappop(max_heap)
        while True:
            if n * (-1) not in min_heap:
                n = heapq.heappop(max_heap)
            else:
                break

        return [n * (-1), m]


if __name__ == "__main__":
    operations = ["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]
    print(solution(operations))