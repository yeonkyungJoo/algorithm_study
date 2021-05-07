# https://programmers.co.kr/learn/courses/30/lessons/42890/solution_groups?language=python3
# 후보키
'''
cadidate key
- unique
- miniality

1 <= len(relation) <= 20
1 <= len(relation[0]) <= 8
all tuple are unique

input: relation (list[list])
output: int

1) all unique
2) partial unique (except unique field)

#data structure
[100, 200, 300, 400, 500, 600]
[a, b, c, d, e, a]
[1, 2, 1, 1, 2, 2]
[2, 2, 3, 1, 3, 2]

len(cols) - len(uniques)개까지의 조합 가능
-> 1 / 1,2 / 1,2,3 / 1,2,3,4
-> 2, 2,3, ...
위에서 만들어진 조합에서 중복이 있으면 안됨
-> itertools.combinations

# solution
## 모든 조합을 다 찾기? brute force
create cols list -> O(n**2)
1 -> 2 -> 3  ...
각각 찾은 조합은 cols_list 에서 제거

조합 생성 -> 모든 값을 다 넣을 필요 없이 index만 넣고 한번에 돌리기

'''
from itertools import combinations
def solution(relation):
    row_len = len(relation)
    col_len = len(relation[0])  

    all_indexes = []
    for i in range(1,col_len+1):
        all_indexes.extend(combinations(range(col_len),i))

    final=[]
    for indexes in all_indexes:
        tmp=[tuple([x[index] for index in indexes]) for x in relation]
        if len(set(tmp))==row_len:
            final.append(indexes)

    answer=set(final[:])
    for i in range(len(final)):
        for j in range(i+1,len(final)):
            if len(final[i])==len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])
                
    return len(answer)

'''
결국 못풀고 포기
'''
