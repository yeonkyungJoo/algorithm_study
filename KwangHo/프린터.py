def solution(priorities, location):
    arr = priorities # 대기목록
    brr = list(0 for i in range(0,len(arr))) # 체크리스트 0초기화
    brr[location] = 1 # 로케이션 값만 1로
    answer = 0
    
    while len(arr)!=0: #모두 인쇄될떄까지
        isCheck = False
        for i in range(1,len(arr)):
            if arr[0] < arr[i] : #현재값보다 크다면 반복 끝
                isCheck = True;
                break
        if isCheck : #현재값 팝해서 그값 뒤에 푸쉬
            t = arr.pop(0)
            arr.append(t)
            t = brr.pop(0) # 로케이션 값 찾기 위해서 체크리스트도 위와 같은 작업
            brr.append(t)
            
        else : #인쇄차례가 되면
            arr.pop(0)  # 팝
            t = brr.pop(0) # 팝
            answer+=1 # 카운트
            if t == 1: # 팝한게 로케이션이랑 같으면 끝
                break
    
    return answer

'''
기본리스트와 location 인덱스체크리스트 만든후
1. 현재값보다 큰값이 있다면 현재값 팝해서 뒤에 푸쉬 (큐)
    +체크리스트도
2. 푸쉬할떄 카운하다가 로케이션 값이랑 같으면 끝!!
'''