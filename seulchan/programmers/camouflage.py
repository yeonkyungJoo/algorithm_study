# https://programmers.co.kr/learn/courses/30/lessons/42578
# 위장
'''
input: list (clothes)
output: int (서로 다른 옷 조합의 수)

clothes: [[name, kind]]
- 1 <= len(clothes) <= 30
- all unique
- 1 <= name, kind <= 20, lowercase + _
- wear at least one
- can wear only one for each kind a day

# solution
## bruth force

pseudo code
# count all clothes -> Counter
c = Counter([x[1] for x in clothes])  # O(n)
c.values() -> [1, 2, 3].. -> (1+1) * (2+1) * (3+1) - 1
return reduce(mul, [x+1 for x in c.values()]) - 1
'''
from collections import Counter
from functools import reduce
from operator import mul
def solution(clothes):
    return reduce(mul,
        [
            value + 1 for value in 
            Counter([x[1] for x in clothes]).values()
        ]
    ) - 1

'''
파이썬 내장함수들로 쉽게 풀었음
리스트 컴프리헨션이 중첩되어서 O(n**2) 이상의 시간복잡도를 가지는게 조금 걸림
'''
