def solution(citations):
    if citations.count(0) == len(citations):
        return 0

    citations = sorted(citations)
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            return len(citations) - i

if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    print(solution(citations))