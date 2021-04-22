def solution(n: int) -> str:
    # 후보
    notation = [1, 2, 4]
    # 최초에 3보다 작으면 재귀함수 호출하지 않고 처리
    if n <= 3:
        remain = n % 3
        # 0 -> 1
        # 1 -> 2
        # 3 -> 4
        return str(notation[remain - 1])
    
    n -= 1
    value = n // 3
    remain = n % 3
    return solution(value) + str(notation[remain])
