from itertools import permutations

def solution(numbers):
    answer = 0
    
    a = set()
    
    #집합만들기
    for i in range(len(numbers)):
        a |= set(map(int, map("".join, permutations(list(numbers), i + 1))))
    a -= set(range(0,2))
    
    #소수만들기
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    
    answer = len(a)
    return answer

'''
문제 이해는 빨리했다.

1. 집합만들기(0과 소수가 아닌 1,2제외)
2. 집합중에서 소수판별하기

집합만들기 너무 복잡하게 짜버려서
찾아보니 set함수가 있었고 permutations가 있었다.
 - 리스트와 갯수를 join해서 map반복
 집합 용어들 다 들어있었다.
 합집합 차집합 교직합 등등
 (  |     -     ^  )

 소수도 에라토스테네스의 체라는게 있어서 그걸로 풀었다.
 모든 배수늘들 지우면 소수만 남는다는 규칙으로
'''