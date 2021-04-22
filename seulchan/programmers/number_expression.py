# https://programmers.co.kr/learn/courses/30/lessons/12924; 숫자의 표현
def solution(n):
    '''
    # pre settings
    - n < 10000
    - only plus possible? -> yes
    - 0 included? -> no
    
    # solution
    ## 1. search and add all
    - n < 10000 -> possible to search all?
    - very inefficient, but possible
    
    ## 2. find exact combination of numbers
    - find possible combinations of sequential number
    - (a) + (a+1) + (a+2) ... (a+b-1) = b(a+(a+b-1))/2 = b(2a + (b-1))/2
    - 2N == b(2a + (b-1)) / 2N/b == 2a + (b-1) / 2N/b - b + 1 == 2a
    - N/b + (1-b)/2 == a
    -> N%b == 0 / (1-b)%2 == 0 -> make this rules to code
    
    - more efficient than solution 1 but similar time complex
    
    # post explanation
    '''
    # solution 2
    answer = 0
    for i in range(n):
        i += 1  # i==0 부터 시작하기 때문에 1 더해줌
        # N%i == 0 / (1-i)%2 == 0 이여야 a가 정수
        if n % i == 0 and (1-i) % 2 == 0:
            answer += 1
            
    return answer
