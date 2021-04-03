# https://programmers.co.kr/learn/courses/30/lessons/64065
# 튜플
import re
from collections import Counter

def solution(s):
    '''
    # pre
    - len(s): 5 ~ 1000000
    
    # solution
    ## 1. use regex & set - X
    - regex to make list of numbers
    - remove duplicate with set
    -> time complex: O(n) for find numbers use regex
    -> can't gurantee order
    
    ## 2. find max len group - X
    - make group inside {}
    - find the largest group -> answer
    -> can't gurantee order
    
    ## 3. made sorted group
    - made all group inside {}
    - sort from smallest
    - add answer from the first by index
    
    # post
    '''
    groups = re.findall('((?:\d,|\d)+)', s)  # ['1,2,3', '1,2,4,3', ...]
    groups.sort(key=lambda x: len(x))  # ['1', '1,2', '1,2,3', ...]
    answer = []
    for group in groups:
        group_list = group.split(',')  # ['1', '2', '3']
        new = list(Counter(group_list) - Counter(answer))[0]
        answer.append(new)
    return [int(x) for x in answer]


'''
처음에 문제를 잘못 이해해서 이상한 방법으로 풀었음
이후에는 regex, counter를 사용했는데 사용하지 않고 풀어봐도 좋을듯하다.
'''

# 인상깊었던 풀이
# 나는 counter를 answer와 비교해서 추가할 int를 찾았지만, 아래 함수에서는 원소의 개수가 많은 순서대로 넣어줌
def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

# strip
# regex를 쓰지 않고 strip 하는 방법
s.lstrip('{').rstrip('}').split('},{')
s[2:-2].split('},{')
