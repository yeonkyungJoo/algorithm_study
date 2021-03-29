def solution(n):
    answer = 0
    
    m=1
    while m <= n :
        s=0
        t=m
        while s+t<=n:
            s+=t
            t+=1
        if s == n :
            answer+=1
            
        m+=1
        
    return answer

'''
m=1
m을 증가시키면서 s에 더해 준다 n보다 작을떄
m=2
위와반복
...
...
총합과 == m 이 같으면 카운트!!

'''