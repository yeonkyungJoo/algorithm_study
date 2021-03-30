# https://programmers.co.kr/learn/courses/30/lessons/12941
def solution(A: list, B: list) -> int:
    '''
    # pre-setting
    len(A) == len(B)
    len(A), len(B) < 1000
    max(A), max(B) < 1000
    - is it impossible to pick k' number from A again
    - it's independent for picking k' number between A and B?
    
    # solution
    ## 1. big-small combination
    - multiply -> Big number should match to small number
    - sort A, B(reversed) and multiply both
    - use zip
    - time comp. O(n)
    
    ## 2. find all combination and compared (X)
    - time comp. O(n**n)
    
    # post-explain
    '''
    # solution 1
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse=True)))
