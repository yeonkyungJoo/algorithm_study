# https://programmers.co.kr/learn/courses/30/lessons/68645
# 삼각 달팽이
'''
1 <= n <= 1000 -> brute force?

width, height(floor) -> n

width: 1, 2, 3, ... n

is it possible to get (x, y) value?
(1, 1) -> 1
(2, 1) -> 2
..
(n, 1) -> n
---
(2, 2) -> 15 -> n*3 -3
(3, 2) -> 16 -> 
...
(n, 2) -> n+1
---
(3, 3) -> 14 -> n*3 - 4

order(index) of result list (n=5)
- 1, 2, 4, 7, 11  -> 1, +1, +2, +3, +4 (..+n-1)   -> fibo(n-1)
- 12, 13, 14, 15 (total n-1)  					  -> fibo(n-1) += 1
- 10, 6, 3 -> ()								  -> minus_fibo(fibo(n-1) - 1) from n-1, till n-2 count
- 5, 8  -> +2/ +3/ fibo()
- 9     -> +1

n=6



# solution
## make helper func (x,y) and calculate all? -> O(n**2)
## create list for floor and append?
## for loop + add to specific index -> too expensive? -> can create [0] * fibo
'''
import itertools
def solution(n):
    # 결과 리스트
    answer = [[0]*i for i in range(1, n+1)]
    
    x, y = -1, 0
    # down, right, up
    index = 1
    for i in range(n):
        for j in range(i, n):
            # down: (x,y) -> (x+1, y)
            if i % 3 == 0:
                x, y = x+1, y
            # right: (x,y) -> (x-1, y-1)
            if i % 3 == 1:
                x, y = x, y+1
            # up: (x,y) -> (x, y+1)
            if i % 3 == 2:
                x, y = x-1, y-1
            answer[x][y] = index
            index += 1
    return list(itertools.chain(*answer))

'''
구현 문제인데 거의 손도 못댐.
조건을 잘 생각하고 푸는 연습이 필요해보임
'''
