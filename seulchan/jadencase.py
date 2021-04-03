# https://programmers.co.kr/learn/courses/30/lessons/12951 JadenCase 문자열만들기
import re

def solution(s):
    '''
    # pre-settings
    - if first letter is not alpha, pass
    
    # solution
    ## 1. make list and loop
    - make list (split)
    - make all first letter to upper
        - 1) for loop inside string -> not efficient
        - 2) use slicing
        - just upper if len == 1
    -> time complexity: O(n) (n=number of word)
    
    ## 2. use regex
    - find space + character
    - change character to upper
    -> more efficient; time complexity -> O(1)
    
    # post
    I expect regex for O(1) but it appears to be O(n)
    '''
    # 2. regex
    def make_upper(s: str) -> str:
        '''
        make " x" -> " X"
        '''
        try:
            return s[0] + s[1].upper()
        except IndexError:
            return s.upper()
    # make all to lower first
    s = re.sub('\w', lambda x: x.group().lower(), s)
    # find first letter | letter right after whitespace
    return re.sub('\s\w|^\w', lambda x: make_upper(x.group()), s)

# 1. make list
def solution(s):
    return' '.join((
        ''.join(x[0].upper() + x[1:].lower()) if len(x) > 1 else x.upper() for x in s.split(' ')
    ))

# 다른사람의 풀이: 내장함수 capitalize 사용
def solution(s):
    return ' '.join(w.capitalize() for w in s.split(' '))

# time complelxity
'''
list solution: O(n)
2 2.567223
4 4.128937
8 7.664672
16 15.013885

regex solution
2 2.474111
4 3.876381
8 7.480944
16 14.684267
'''
