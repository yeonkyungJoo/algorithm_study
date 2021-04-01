def solution(people, limit):
    answer = 0
    
    people.sort()
    a=0 #0
    b=len(people)-1 #최대
    c=0 #카운트
    while a < b :
        if people[a]+people[b] <= limit:
            a+=1
            b-=1
        else :
            b-=1
        c+=1
    if a==b : c+=1 #마지막에 하나만 카운트하므로 같으면 카운트 하나더
    answer = c
    return answer

'''
처음에 모든 경우의 수를 생각하는 완전탐색으로 하는데
자꾸 재귀깊이횟수 초과랑 시간초과가 보니깐 최대2명이였었다ㅠ

정렬하고
최소+최대 조합이 2명조합 갯수가 최대 이므로
리미트를 넘지않으면 a++ b-- 카운트
넘으면 b-- 카운트 b쪽을 카운트하는것
a는 리미트보다 적은수를 많나기 위해 킵느낌으로!!
'''