def solution(skill, skill_trees):
    answer = 0
    n = len(skill_trees)

    for i in range(n):
        a = skill_trees[i] #하나씩 받아오기
        m = len(a) #a길이
        t1 = "" 
        t2 = ""
        c = 1 #순서대로 추가햇을때의 카운트
        for j in range(m) :
            
            if a[j] in skill : #포함되 스킬을 모조리 추가한다.
                t1 += a[j]
                if t1 in skill[:c] : #순서에 맞게 하나씩 추가
                    t2 += a[j]       #첫순서가 맨뒤에 있으면 하나만 추가 된다.
                    c+=1
        
        if t1 == t2 : # 비교해서 카운트
            answer+=1
            
    return answer

'''
문제이해후 풀이가 여러방식이 나왔다.
그래서 좀더 깔끔하고 괜찮은 방법으로 풀었다.

1. 스킬트리에 스킬이 포함되면 t1에 추가추가
2. t2에는 순서대로 추가
3. 마지막에 t1 == t2 비교해보면 순서대로 체크가능!!
'''