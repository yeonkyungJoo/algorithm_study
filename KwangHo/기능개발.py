def solution(progresses, speeds):
    answer = []
    
    maxx = -1
    cnt = 0
    
    
    for i in range(len(progresses)):
        t = (100-progresses[i]) / speeds[i] # 일수 구하기
        if t%1!=0: #100넘어가면 +1
            t += 1
        t = int(t)
        
        if maxx == -1 : #초기화
            maxx = t
        
        if maxx >= t : #완료일수보다 작으면 카운트
            cnt+=1
        else :         #완료일수보다 크면 현재 카운트 추가하고 새로카운트 시작!!
            answer.append(cnt)
            cnt = 1
            maxx = t
    answer.append(cnt) #마지막 일수를 계산하는 조건이 없기때문에 추가!!   
        
    return answer

'''
스택/큐 관련 문제이겟거니 했는데
반복문 돌면서 조건처리만 잘해주면 되겟다 싶었다.

처음 들어온 기능의 완료일수를 구하고,
다음번 다음번이 완료일수보다 작으면 카운트
아니면 기존카운트 추가하고 카운트 초기화
그리고 마지막에 카운트 추가 한번더!!

'''