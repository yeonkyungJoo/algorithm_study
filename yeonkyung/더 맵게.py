import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)

    while True:
        f1 = heapq.heappop(scoville)
        if len(scoville) == 0 and f1 < K:
            return -1
        if f1 >= K:
            break
        f2 = heapq.heappop(scoville)
        heapq.heappush(scoville, f1 + (f2 * 2))
        count += 1

    return count

if __name__ == "__main__":
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    print(solution(scoville, K))