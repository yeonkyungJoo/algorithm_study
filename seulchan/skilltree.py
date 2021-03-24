# https://programmers.co.kr/learn/courses/30/lessons/49993#fn1
import re

def solution(skill, skill_trees):
    '''
    방법1: stack
    각 스킬 트리별로 하나씩 빼면서 순서에 맞는지 확인
    
    방법2: text replace
    필요없는 텍스트를 모두 제거하고 남은 텍스트가 일치하는지 확인
    '''
    answer = 0
    # 방법2: text replace
    for x in skill_trees:
        # regex로 skill에 들어가지 않은 텍스트 제거
        sub = re.sub(f'(?![{skill}])[A-Z]', '', x)
        # 개수가 x개이면 무조건 스킬의 skill[:x-1]이랑 같아야됨
        if skill[:len(sub)] == sub:
            answer += 1
    return answer

# 축약 버전
def solution(skill, skill_trees):
    answer = 0
    # 방법2: text replace
    for x in skill_trees:
        # regex로 skill에 들어가지 않은 텍스트 제거
        sub = re.sub(f'(?![{skill}])[A-Z]', '', x)
        # 개수가 x개이면 무조건 스킬의 skill[:x-1]이랑 같아야됨
        if skill[:len(sub)] == sub:
            answer += 1
    return answer
