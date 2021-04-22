# 괄호 변환: https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3
def divide(p: str):
    '''
    괄호 p를 받아 u, v 반환
    - u: the last balanced (cannot be divided more)
    - v: rest ('' possible)
    '''
    open_p = 0
    close_p = 0
    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[:i + 1], p[i + 1:]


# 문자열 u가 올바른 괄호 문자열인지 확인하는 함수
def is_complete(p: str) -> bool:
    count = 0
    for x in p:
        if count < 0:
            return False
        if x == '(':
            count += 1
        else:
            count -= 1
    return count == 0

def solution(p):
    '''
    # pre-settings
    - balance -> right
    - balance -> divide into "u" (balanced) + "vmu" (can be empty)
    ??? 이해가 안됨
    
    # solution
    ## 1. create code from explain
    
    ## 2. stack?
    - use stack to make "u" and "v"
    
    ## 3. recursion
    - 
    
    # post explain
    '''
    # recursion
    
    # stack
    # else divide(p) -> u, v / stack.append(v), stack.append(u)
    # -> x = stack.pop() / divide(x) -> append(v), (u)
    # if u is not complete -> divide(u)
    # if v is not complete -> divide(v)
    if p == '' or is_complete(p):
        return p
    
    u, v = divide(p)
    # u가 올바른 문자열이라면
    if is_complete(u):
        # v에 대해 1단계부터 수행
        return u + solution(v)
    
    else:
        # u가 올바른 문자열이 아니라면
        # 4-1 ~ 4-3: ( + v에대해 1단계부터 수행한결과 + )
        answer = f'({solution(v)})'

        # 4-4: u의 첫번째, 마지막 제거하고 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙이기
        u = u[1:-1]
        for x in u:
            if x == '(':
                answer += ')'
            else:
                answer += '('
        return answer 

