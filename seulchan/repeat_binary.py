# https://programmers.co.kr/learn/courses/30/lessons/70129
# 이진 변환 반복하기
'''
x = string (0 and 1)
remove all 0
len(c)=number of 1 -> binary
...
0111010 -> 1111 -> len(1111) = 4 -> "100"
100 -> 1 -> len(1) = 1

input: string s, 1 < len(s) < 1500000, at least 1
output list [number of translate, number of removed 0]

# solution

translate, removed = 0, 0
# count removed
removed += Counter(s)[0]  # Counter() -> O(n)
s = replace('0', '1', s)	# replace -> O(n)
num = len(s)
b_string = str(bin(num))
if 0 in set(b_string):  # set
	translate += 1
	solution(b_string)
else:
	return [translate, removed]

# second solution

translate, removed = 0, 0
while '0' in set(s):
    removed += Counter(s)['0']
    s = re.sub('0', '', s)
    
    b_string = str(bin(len(s)))
    translate += 1
    

time: O(2n) -> O(n*translate) -> O(n)
space: O(n)
'''
import re
from collections import Counter

def solution(s):
    translate, removed = 0, 0
    if s in ['1', '01']:
        return [translate, removed]
    
    while s not in ['1', '01']:
        removed += Counter(s)['0']
        s = re.sub('0', '', s)
        s = str(bin(len(s)))[2:]
        translate += 1
    return [translate, removed]

# time complex 나은 코드
def solution(s):
    translate, removed = 0, 0
    while s != '1':
        num = s.count('1')
        removed += len(s) - num
        s = bin(num)[2:]
        translate += 1
    return [translate, removed]

# recursion error
# def solution(s):
#     # 1. recursion -> maximum recursion error
#     if s == '1':
#         return [tranlate, removed]
#     translate, removed = 0, 0
#     removed += Counter(s)['0']
#     s = re.sub('0', '', s)
    
#     b_string = str(bin(len(s)))
#     translate += 1
#     solution(b_string)

'''
- 처음에 recursion을 사용했는데 maximum recursion error가 나서 while으로 변경
- time, space complexity 계산을 잘 못하겠음
    - Counter(), re.sub(), bin() time complexity 확인 필요
    - regex: O(n)
    - Counter: O(n)
- str(bin())에서 0b가 prefix로 붙는걸 몰라서 print 해보고 알았다
- Counter, bin() 용법이 헷갈렸음
- bin()가 str을 반환하므로 str(bin()) 할필요 없었음
- re.sub 대신 s.count('1')을 사용해도 됨 (O(n)
- s.count('1')을 전체 길이에서 빼주면 더 좋은 코드가 됨: O(2n) -> O(n)

'''
