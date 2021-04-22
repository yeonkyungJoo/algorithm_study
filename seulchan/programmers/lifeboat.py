# https://programmers.co.kr/learn/courses/30/lessons/42885 구명보트
from collections import deque
def solution(people, limit):
    '''
    # pre-settings
    - people: 1 ~ 50000
    - people[x]: 40 ~ 240
    - limit: 40 ~ 240
    
    # solution
    ## 1. sort -> sequentially board
    - sort (reversed?)
    - for loop and plus
    
    ## 2. sort reversed and send heavy with light
    
    # post-explain
    '''
    people.sort(reverse=True)
    pq = deque(people)
    
    answer = 0
    
    while pq:
        first = pq.popleft()
        # 무거운 사람이 limit 절반 이하면 무조건 두명씩 보낼수있음 -> 남은사람 % 2
        try:
            last = pq[-1]
            # 두명 더해서 리밋을 넘으면 보내기
            if first + last <= limit:
                pq.pop()
        except IndexError:
            pass
            
        answer += 1
    return answer
