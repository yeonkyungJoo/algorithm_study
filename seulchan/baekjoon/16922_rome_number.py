'''
로마 숫자 N개를 사용해서 만들수있는 서로 다른 수
로마 숫자: I, V, X, L (1, 5, 10, 50)

not considering order
ex. IX -> I + X -> 11

all possible combinations -> itertools.combinations_with_replacements
1 -> 4
2 -> 4 + 3 + 2 + 1

- should considering duplicate

# solution

## brute force
- create combinations
- create integer from string
- append it to set
- return len(set)

def sum_rome(array: list) -> int:
    # sum all the array from rome list
    c = Counter(array)   # O(n)?
    return 1 * c['I'] + 5 * c['V'] + 10 * c['X'] + 50 * c['L']


int_set = set()
coms = combinations_with_replacements('IVXL', N)

for com in coms:  # O(n)
    # sum all
    s = sum_rome(com)
    int_set.append(s)
return len(int_set)

-> time complextiy: O(n**2)
-> space complexity: O(n**2) # coutner, set

can be better without counter?
'''
from collections import Counter
from itertools import combinations_with_replacement

def sum_rome(array: tuple) -> int:
    # sum all the array from rome list
    c = Counter(array)   # O(n)?
    return 1 * c['I'] + 5 * c['V'] + 10 * c['X'] + 50 * c['L']

def solution(N: int) -> int:
    int_set = set()
    coms = combinations_with_replacement('IVXL', N)

    for com in coms:  # O(n)
        # sum all
        s = sum_rome(com)
        int_set.add(s)
    return len(int_set)

N = int(input())
print(solution(N))

if __name__ == '__main__':
    print(solution(10))
