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
    # 제거할 regex 생성
    reg = f'(?![{skill}])[A-Z]'
    # regex로 제거
    removed = (re.sub(reg, '', x) for x in skill_trees)
    
    # 개수가 x개이면 무조건 스킬의 skill[:x-1]이랑 같아야됨
    for s in removed:
        skill_count = len(s)
        if skill[:skill_count] == s:
            answer += 1
    return answer
