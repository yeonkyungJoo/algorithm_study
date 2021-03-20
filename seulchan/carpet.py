# https://programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    # 총 개수 n * m 가능
    # 2n + 2m -4 개수가 yellow면 True
    # n * m = (brown + yello)
    # n + m = (brown + 4) // 2
    m = 1
    while True:
        n = ((brown + 4) // 2) - m
        if n * m == (brown + yellow):
            return [n, m]
        m += 1
