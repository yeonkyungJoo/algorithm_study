from collections import deque
from itertools import combinations

def solution(relation):
    answer = 0
    n_row = len(relation)
    n_col = len(relation[0])  
    
    #조합만들기
    candidates=[]
    for i in range(1,n_col+1):
        candidates.extend(combinations(range(n_col),i))
    
    #조합중에 겹쳐지는것이 없으면 추가
    final=[]
    for keys in candidates:
        tmp=[tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp))==n_row:
            final.append(keys)
    
    #최소성을 위한 제거작업
    answer=set(final[:]) #집합으로 만들어놓고 
    #2중반복
    for i in range(len(final)):
        for j in range(i+1,len(final)):
            #현재 길이와 , 교직합 길이가 같으면 중복되는게 있는거니깐 지워도 됨!!
            if len(final[i])==len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j]) #집합삭제
    
    return len(answer)


'''
풀다가 난장판 200줄가까이돼서 3개 케이스 남겨놓고
내코드를 내가 헷갈려서 포기!!
풀이보고 정리해서 코드작업!!
나중에 다시 풀기위해 제출은 패스!!
'''