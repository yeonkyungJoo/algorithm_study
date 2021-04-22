# https://programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    answer = True
    # brute force
    count = 0
    for x in s:
        if x == '(':
            count += 1
            continue
        # ')'일 경우 
        # count가 0이면 무조건 false
        if not count:
            return False
        # count가 1 이상이면 -1
        count -= 1
    return not count
