# https://www.ibric.org/myboard/read.php?Board=news&id=270333 
def solution(citations):
    n = len(citations)
    citations.sort()
    # [0, 1, 3, 5, 6]
    # 탐색하면서
    for i, c in enumerate(citations):
        # 논문 개수랑 해당논문 포함 큰 개수를 비교
        # 논문개수가 크면 해당 개수 반환
        larger_than = n - i
        if c >= larger_than:
            return larger_than 
    return 0
