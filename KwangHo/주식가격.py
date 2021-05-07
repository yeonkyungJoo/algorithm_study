def solution(prices):
    answer = []
    n = len(prices)
    
    for i in range(0,n):
        answer.append(0) #값 추가 하면서 0으로 초기화
        for j in range(i+1,n): # 기준값 다음값 부터 ~ 길이까지
            if prices[i] <= prices[j]: # 비교해서 떨어지지 않으면 카운트
                answer[i]+=1
            else:                    # 떨어지면 1초카운트 하고 탈출
                answer[i]+=1
                break
                
    return answer

'''
2중 반복분 돌면서 비교값 체크해서
떨어지지 않을때는 카운트
떨어지면 끝이니깐 1초카운트하고 탈출
입출력예의 3초시점을 캐치해서 쉽게 풀었던거 같다.
'''