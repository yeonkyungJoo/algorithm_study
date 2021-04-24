# https://programmers.co.kr/learn/courses/30/lessons/17687
# n진수 게임
'''
10;
2; 0 1 10 11 100 101 110 111 1000 -> 1, 2, 4, 8... -> 
3; 0 1 2 10 11 12 20 21 22 100 ...
...
16; 

input; n, t(count of answer), m (people), p (order)
output; string

n: 2 ~ 16
0 < t <= 1000
2 <= m <= 100


# solution
## brute force
- n진법: 1*(n*1) + 2*(n*2) + 3*(n*3) ... 


- total number of string: t*m -> n진법의 경우 

- create all n till x
    - find minimum x count
- make string from x
- find 'm'th string from p till 't' count
'''
def solution(n, t, m, p):
    HEX = '0123456789ABCDEF'
    def numeral(number: int, base: int) -> str:
        q, r = divmod(number, base)
        n = HEX[r]
        return numeral(q, base) + n if q else n
    result = ''
    x = 0
    while True:  # 더 합리적으로 조금만 돌릴 수 있으면 좋음
        # 2, 8, 16진법은 내장함수 사용
        if n == 2:
            result += bin(x)[2:]
        elif n == 8:
            result += oct(x)[2:]
        elif n == 16:
            result += hex(x)[2:].upper()
        else:
            result += numeral(x, n)
        x += 1
        if len(result) > t*m:
            break
        
    # find m'th string from p till 't'
    return result[p-1:m*t:m]

'''
가장 조금만 순회할 수 있는 x를 찾다가 시간을 많이 씀
매번 result의 길이를 확인하지 않고 수학적으로 구할 수 있을거같은데
문제 푸는데 시간이 오래걸릴 것 같으면 과감하게 포기하고 답을 내는게 좋아보임
'''
