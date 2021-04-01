# https://programmers.co.kr/learn/courses/30/lessons/42586; 기능 개발
from collections import deque
def solution(progresses, speeds):
    progresses, speeds = deque(progresses), deque(speeds)
    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100: 
            progresses.popleft()
            speeds.popleft()
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
